#!/usr/bin/env python3
"""queue.py — planning helper for the orchestrator. Read-only; touches no game data.

Builds the two work queues the survey needs (CLAUDE.md §4 step 1):

  battle   every chunk with no tl/battle/chunk_NNN.txt and no pending/chunk_NNN.txt,
           with JP chars, headroom and the §0.2 budget ratio; ratio < 1.6 is tier A (blocked).

  script   every dumps/script_unique.txt line not yet in tl/script/*.tsv, mapped to the
           `=== BANK n` sections it lands in, with the projected growth per bank and the
           blocked/free verdict, then grouped into batches.

Usage:
    python3 tools/queue.py battle
    python3 tools/queue.py script [--batch-size 50] [--batches 4]
    python3 tools/queue.py banks
"""
import os, re, sys, math

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import assemble as A

SLOT     = A.SCRIPT_SLOT      # 8192
BANK     = A.BANK             # 0xA000
RESERVE  = 500                # bytes kept free in every bank
GROWTH   = 2.10               # English chars per Japanese char — MEASURED over the 151
                              # lines already shipped (aggregate 9,595/4,482). The prompt's
                              # 'disciplined draft' is ~1.75x; use that only when a translator
                              # is told the unit is bank-tight.
COLS     = 24


# ------------------------------------------------------------------ battle

def battle_rows():
    _, chunks, order = A.split_battle(A.read(os.path.join(A.DUMPS, 'battle_dump.txt')))
    done    = set(A.load_battle_tl())
    parked  = {int(m.group(1)) for m in
               (re.match(r'chunk_(\d+)\.txt$', f) for f in os.listdir(os.path.join(ROOT, 'pending')))
               if m}
    rows = []
    for idx in order:
        header, body = chunks[idx]
        text = ''.join(l for l in body if not A.is_structural(l))
        ja   = len(re.sub(r'\{[^}]*\}', '', text))
        hm   = re.search(r'headroom (\d+)', header)
        head = int(hm.group(1)) if hm else 0
        if not ja:
            continue
        tag_bytes = (SLOT - head) - 2 * ja
        budget    = (SLOT - tag_bytes) / 2.0
        ratio     = budget / ja
        rows.append(dict(idx=idx, ja=ja, head=head, tags=tag_bytes,
                         budget=int(budget), ratio=ratio,
                         state='done' if idx in done else 'parked' if idx in parked else 'open'))
    return rows


def tier(r):
    return 'A' if r < 1.6 else 'B' if r < 2.5 else 'C' if r < 4.0 else 'D' if r < 6.5 else 'E'


def cmd_battle():
    rows = battle_rows()
    open_ = [r for r in rows if r['state'] == 'open']
    print('BATTLE QUEUE — %d open of %d chunks with text' % (len(open_), len(rows)))
    print(' chunk  tier   JP  headroom  ratio   budget(EN chars)')
    for r in sorted(open_, key=lambda r: r['idx']):
        print('   %3d     %s %5d    %6d   %5.2f   %6d%s'
              % (r['idx'], tier(r['ratio']), r['ja'], r['head'], r['ratio'], r['budget'],
                 '   BLOCKED (tier A)' if r['ratio'] < 1.6 else ''))
    disp = [r for r in open_ if r['ratio'] >= 1.6]
    print('\ndispatchable %d, blocked %d, JP chars remaining %d'
          % (len(disp), len(open_) - len(disp), sum(r['ja'] for r in open_)))


# ------------------------------------------------------------------ script

def bank_free():
    """{bank: free bytes} from the merged dump, via bankmeasure's own emitter."""
    import bankmeasure
    path = os.path.join(A.BUILD, 'script_dump_merged.txt')
    if not os.path.exists(path):
        sys.exit('run `python3 tools/assemble.py merge` first')
    used = bankmeasure.measure(path)
    return {b: BANK - u for b, u in used.items()}


def script_rows():
    uni = [l for l in A.read(os.path.join(A.DUMPS, 'script_unique.txt')).split('\n')
           if l.strip() and not l.startswith('#')]
    rows = []
    for i, l in enumerate(uni, 1):
        p = l.split('\t')
        if len(p) >= 2:
            rows.append(dict(n=i, count=int(p[0]), jp=p[1]))
    pairs, _ = A.load_script_tl()
    for r in rows:
        r['done'] = r['jp'] in pairs

    # bank membership: a dump line is exactly <key>{FFFF}
    where = {}
    cur = None
    order = []
    for raw in A.read(os.path.join(A.DUMPS, 'script_dump.txt')).split('\n'):
        m = re.match(r'=== BANK (\d+) @', raw)
        if m:
            cur = int(m.group(1))
            continue
        if cur is None or not raw.endswith('{FFFF}'):
            continue
        key = raw[:-6]
        where.setdefault(key, {}).setdefault(cur, 0)
        where[key][cur] += 1
        order.append((cur, key))
    for r in rows:
        r['banks'] = where.get(r['jp'], {})
    return rows, order


def growth(r, ratio=GROWTH):
    """Projected extra bytes per instance: English at GROWTH x JP, plus 2 per added row break."""
    jp    = len(re.sub(r'\{[^}]*\}', '', r['jp']))
    en    = ratio * jp
    rows_jp = math.ceil(jp / COLS) if jp else 0
    rows_en = math.ceil(en / (COLS - 1)) if en else 0
    return int(2 * (en - jp) + 2 * max(0, rows_en - rows_jp))


def allocate(todo, free, ratio=GROWTH, reserve=RESERVE):
    """Greedy per-bank budget allocation.

    Every bank gets `free - reserve` bytes to spend. Lines are offered highest
    instance-yield-per-byte first; a line is taken only if EVERY bank it lands in can
    still pay for its growth there. What is left over is genuinely bank-blocked.
    """
    budget = {b: max(0, f - reserve) for b, f in free.items()}
    cap = dict(budget)

    def density(r):
        # multi-dimensional knapsack greedy: instances gained per unit of SCARCITY consumed.
        # A byte spent in bank 41 (353 free) costs far more than one in bank 26 (39,889).
        g = growth(r, ratio)
        pressure = sum(g * n / max(1.0, cap.get(b, 1)) for b, n in r['banks'].items())
        return r['count'] / pressure if pressure else 0.0

    taken, blocked = [], []
    for r in sorted(todo, key=lambda r: (-density(r), -r['count'])):
        g = growth(r, ratio)
        need = {b: g * n for b, n in r['banks'].items()}
        if all(budget.get(b, 0) >= v for b, v in need.items()):
            for b, v in need.items():
                budget[b] -= v
            taken.append(r)
        else:
            blocked.append(r)
    return taken, blocked, budget


def cmd_script(batch_size=50, nbatches=None):
    rows, order = script_rows()
    free = bank_free()
    todo = [r for r in rows if not r['done'] and r['banks']]
    orphan = [r for r in rows if not r['done'] and not r['banks']]

    demand = {}
    for r in todo:
        g = growth(r)
        for b, n in r['banks'].items():
            demand[b] = demand.get(b, 0) + g * n

    print('SCRIPT QUEUE — %d untranslated unique lines (%d instances)'
          % (len(todo), sum(r['count'] for r in todo)))
    print('\ngrowth model: English at %.2fx Japanese characters (measured on shipped work),'
          ' %d bytes reserved per bank' % (GROWTH, RESERVE))
    print('\nbank pressure if EVERY remaining line were translated:')
    print(' bank    free   demand   verdict')
    for b in sorted(demand):
        over = demand[b] - (free.get(b, 0) - RESERVE)
        print('  %3d  %6d   %6d   %s'
              % (b, free.get(b, 0), demand[b], 'OVER by %d' % over if over > 0 else 'ok'))

    ok, blocked, left = allocate(todo, free)
    print('\nAFTER ALLOCATION (greedy, highest instances per byte first)')
    print('  translatable now : %4d lines, %4d instances'
          % (len(ok), sum(r['count'] for r in ok)))
    print('  bank-blocked     : %4d lines, %4d instances  -> pending/script/'
          % (len(blocked), sum(r['count'] for r in blocked)))
    if orphan:
        print('  no bank match    : %4d lines  (key drift — investigate)' % len(orphan))
    tightest = sorted(left.items(), key=lambda kv: kv[1])[:6]
    print('  budget left after allocation: %s'
          % ', '.join('bank %d:%d' % (b, v) for b, v in tightest))
    if blocked:
        print('  worst blocked lines (instances, banks):')
        for r in sorted(blocked, key=lambda r: -r['count'])[:8]:
            print('    line %4d  %3d inst  banks %s  jp %d chars'
                  % (r['n'], r['count'], sorted(r['banks']), len(re.sub(r'\{[^}]*\}', '', r['jp']))))

    # batching: seed on the highest-count line, then its nearest neighbours in the dump
    pos = {}
    for i, (b, k) in enumerate(order):
        if k not in pos:
            pos[k] = i
    pool = sorted(ok, key=lambda r: (-r['count'], pos.get(r['jp'], 0)))
    taken, batches = set(), []
    for seed in pool:
        if seed['n'] in taken or (nbatches and len(batches) >= nbatches):
            continue
        i = pos.get(seed['jp'], 0)
        near = sorted((r for r in ok if r['n'] not in taken and r['n'] != seed['n']),
                      key=lambda r: abs(pos.get(r['jp'], 0) - i))
        batch = [seed] + near[:batch_size - 1]
        taken |= {r['n'] for r in batch}
        batches.append(batch)
    for k, batch in enumerate(batches, 1):
        bset = sorted({b for r in batch for b in r['banks']})
        jp = sum(len(re.sub(r'\{[^}]*\}', '', r['jp'])) for r in batch)
        print('\nbatch %d: %d lines, %d instances, %d JP chars, banks %s'
              % (k, len(batch), sum(r['count'] for r in batch), jp, bset))
        print('  unique lines: %s'
              % ','.join(str(r['n']) for r in sorted(batch, key=lambda r: r['n'])))
        print('  free in those banks: %s'
              % ', '.join('%d:%d' % (b, free.get(b, 0)) for b in bset))


def cmd_banks():
    free = bank_free()
    for b in sorted(free):
        print('  bank %2d  free %6d' % (b, free[b]))


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a or a[0] == 'battle':
        cmd_battle()
    elif a[0] == 'script':
        bs = int(a[a.index('--batch-size') + 1]) if '--batch-size' in a else 50
        nb = int(a[a.index('--batches') + 1]) if '--batches' in a else None
        cmd_script(bs, nb)
    elif a[0] == 'banks':
        cmd_banks()
    else:
        sys.exit(__doc__)
