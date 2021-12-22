import re
from collections import Counter

def extract(line):
    return list(map(int, re.findall(r"-?\d+", line)))

input = open("inputs/day19.txt", "r").read().split("\n\n")

# Hardcoded orientations
signs = (1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1), (-1, 1, 1), (-1, 1, -1), (-1, -1, -1), (-1, -1, 1)
perms = (0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)

# Input parsing
arr = [list(map(extract, line.strip().split("\n")[1:])) for line in input]

points = set(map(tuple, arr.pop(0)))
unknown = [True] * len(arr)
beacons = []
while any(unknown):
    # Go through the remaining scanners
    for ind, (pts, identified) in enumerate(zip(arr, unknown)):
        if not identified:
            continue
        found = False
        # Try all axis directions
        for sign in signs:
            if found:
                break
            tmp = [(x * sign[0], y * sign[1], z * sign[2]) for x, y, z in pts]
            # Try all axis orientations
            for perm in perms:
                RES = []
                res = []
                # Attempt to combine the points pairwise and see if 12 points line up
                for i in tmp:
                    i = x, y, z = i[perm[0]], i[perm[1]], i[perm[2]]
                    res.append(i)
                    RES.extend(((ax + x, ay + y, az + z) for ax, ay, az in points))
                # The most common point should be where a beacon lies
                (cx, cy, cz), quantity = Counter(RES).most_common(1)[0]
                if quantity >= 12:
                    # Found a beacon!
                    unknown[ind] = False
                    # Update the list of known points with the beacon's position
                    points |= {(cx - x, cy - y, cz - z) for x, y, z in res}
                    found = True
                    beacons.append((cx, cy, cz))
                    break

def manhattan(a, b):
    return sum(abs(i - j) for i, j in zip(a, b))

print(len(points))
print(max(manhattan(a, b) for a in beacons for b in beacons))

