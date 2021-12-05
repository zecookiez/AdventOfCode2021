import re
from collections import defaultdict

def extract_int(line):
    return list(map(int, re.findall(r"-?\d+", line)))

input = open("inputs/day05.txt", "r").readlines()

grid = defaultdict(int)
diag = defaultdict(int)
for line in input:
    x1, y1, x2, y2 = extract_int(line)
    if x1 == x2:
        # Horizontal line
        for y in range(min(y1, y2), max(y1, y2) + 1):
            grid[x1, y] += 1
    elif y1 == y2:
        # Vertical line
        for x in range(min(x1, x2), max(x1, x2) + 1):
            grid[x, y1] += 1
    # Diagonal Line
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    if dx == dy:
        # Determine direction
        Dx = 1 if x1 < x2 else -1
        Dy = 1 if y1 < y2 else -1
        # +1 to include endpoint (dx is the length)
        for _ in range(dx + 1):
            diag[x1, y1] += 1
            x1 += Dx
            y1 += Dy

def count_overlap(grid):
    # Exclude the number of points with just one line segment
    return len(grid) - [*grid.values()].count(1)

part_1 = count_overlap(grid)

for key, val in diag.items():
    grid[key] += val

print(part_1, count_overlap(grid))
