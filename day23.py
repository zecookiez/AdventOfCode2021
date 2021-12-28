from collections import defaultdict
from heapq import heappush, heappop

# It was easier to input the puzzle input by hand...
# I've already spent a few hours whittling this down to 20 seconds (it used to take over a minute)
# Maybe someday I will find a better way to do this but that day is not today :(

spots = {(0, 0), (0, 1), (0, 3), (0, 5), (0, 7), (0, 9), (0, 10)}
A = [(2, 8), (3, 6), (4, 4), (4, 8)] # Turn 4->2 for Part 1
B = [(2, 6), (3, 4), (4, 2), (4, 6)] # Turn 4->2 for Part 1
C = [(1, 6), (1, 8), (2, 4), (3, 8)]
D = [(1, 2), (1, 4), (2, 2), (3, 2)]
TGT_A = [(1, 2), (2, 2), (3, 2), (4, 2)]
TGT_B = [(1, 4), (2, 4), (3, 4), (4, 4)]
TGT_C = [(1, 6), (2, 6), (3, 6), (4, 6)]
TGT_D = [(1, 8), (2, 8), (3, 8), (4, 8)]
TARGET = [TGT_A, TGT_B, TGT_C, TGT_D]

best = defaultdict(int)
queue = [(0, [A, B, C, D], tuple([tuple(A), tuple(B), tuple(C), tuple(D)]))]

def reachable(cur, tgt, other):
    # Moving from pit to pit
    if cur[0] == 0 == tgt[0]: return False
    cx, cy = cur
    TGT = tgt[1]
    # Not blocked in hallway
    return all(not any(cy < y < TGT or TGT < y < cy for x, y in i if x == 0) for i in other)

# Calculates the "manhattan" distance from one location to another
def man(a, b, mul):
    return mul * (a[0] + b[0] + abs(a[1] - b[1]))

# For debugging purposes
def visualize(a, b, c, d):
    grid = [
        "...........",
        "##.#.#.#.##",
        " #.#.#.#.# ",
        " #.#.#.#.# ",
        " #.#.#.#.# "
    ]
    grid = list(map(list, grid))
    for x, y in a: grid[x][y] = "A"
    for x, y in b: grid[x][y] = "B"
    for x, y in c: grid[x][y] = "C"
    for x, y in d: grid[x][y] = "D"
    for i in grid: print("".join(i))
    return

# For the dijkstra
def push(dist, nxt):
    HASH = tuple(map(tuple, nxt))
    if HASH not in best or best[HASH] > dist:
        best[HASH] = dist
        heappush(queue, (dist, nxt, HASH))

while queue:
    dist, pts, HASH = heappop(queue)
    if best[HASH] < dist:
        continue
    if pts == TARGET:
        print(dist)
        break
    # Move from pit to hallway
    OCCUPIED = set()
    grouped = defaultdict(list)
    cand_src = []
    for cur in pts:
        for pt in cur:
            grouped[pt[1]].append(pt[0])
    grouped_min = {i: min(j) for i, j in grouped.items()}
    for i, cur in enumerate(pts):
        OCCUPIED.update(set(cur))
        for j, (cx, cy) in enumerate(cur):
            # Nothing above
            if grouped_min[cy] == cx:
                cand_src.append((cx, cy, i, j))
    for tgt in spots - OCCUPIED:
        for cx, cy, i, j in cand_src:
            if reachable((cx, cy), tgt, pts):
                nxt = list(map(list, pts))
                nxt[i][j] = tgt
                nxt[i].sort()
                push(dist + man((cx, cy), tgt, 10**i), nxt)
    # Move from hallway to pit
    for i, (cur, TGT) in enumerate(zip(pts, TARGET)):
        CUR = set(cur)
        exc = OCCUPIED - CUR
        if all(j not in exc for j in TGT):
            vacant = len(grouped[TGT[0][1]])
            if vacant < len(TGT):
                tgt = TGT[~vacant]
                cand = []
                for j, (cx, cy) in enumerate(cur):
                    # Nothing above
                    if grouped_min[cy] == cx:
                        cand.append((cx, cy, i, j))
                if tgt not in OCCUPIED:
                    for cx, cy, i, j in cand:
                        if reachable((cx, cy), tgt, pts):
                            nxt = list(map(list, pts))
                            nxt[i][j] = tgt
                            nxt[i].sort()
                            push(dist + man((cx, cy), tgt, 10**i), nxt)