import re

def extract(line):
    return list(map(int, re.findall(r"\d+", line)))

pts, folds = open("inputs/day13.txt", "r").read().split("\n\n")
pts = [extract(line) for line in pts.split("\n")]

# Utility function to fold the points
def fold_x(pts, X):
    return [(x if x < X else X - (x - X), y) for x, y in pts]
def fold_y(pts, Y):
    return [(x, y if y < Y else Y - (y - Y)) for x, y in pts]

first_line = True # Part 1 flag
for line in folds.strip().split("\n"):
    if "x" in line:
        # Fold in x-axis
        pts = fold_x(pts, extract(line)[0])
    else:
        # Fold in y-axis
        pts = fold_y(pts, extract(line)[0])
    # Part 1
    if first_line:
        print(len(set(pts)))
        first_line = False

# Output final grid of points
W = max([*zip(*pts)][0]) + 1
H = max([*zip(*pts)][1]) + 1
grid = [[0] * W for i in range(H)]
for x, y in pts:
    grid[y][x] = 1
for row in grid:
    print("".join(" #"[col] for col in row))
