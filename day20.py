
ID, grid = open("inputs/day20.txt", "r").read().split("\n\n")

pixels = {}
for x, row in enumerate(grid.split()):
    for y, col in enumerate(row):
        pixels[x, y] = 1 if col == "#" else 0

def get_bound(pix):
    x, y = zip(*pix)
    return (min(x) - 1, max(x) + 2), (min(y) - 1, max(y) + 2)

def apply(pixels, default):
    res = {}
    (xL, xR), (yL, yR) = get_bound(pixels)
    for x in range(xL, xR):
        for y in range(yL, yR):
            out = 0
            for dx in x - 1, x, x + 1:
                for dy in y - 1, y, y + 1:
                    out = out * 2 + pixels.get((dx, dy), default)
            res[x, y] = 1 if ID[out] == "#" else 0
    return res

for _ in range(50):
    pixels = apply(pixels, _ % 2)
    if _ == 1:
        print(sum(pixels.values()))

print(sum(pixels.values()))
