input = open("inputs/day09.txt", "r").readlines()

grid = []
for line in input:
    grid.append(list(map(int, line.strip())))

H = len(grid)
W = len(grid[0])

def get_adjacent(x, y):
    for nx, ny in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
        if 0 <= nx < H and 0 <= ny < W:
            yield (nx, ny)

# Identify all basin locations
basin = []
total = 0
for x in range(H):
    for y in range(W):
        cur = grid[x][y]
        if all(cur < grid[nx][ny] for nx, ny in get_adjacent(x, y)):
            total += cur + 1
            basin.append((x, y))

# Perform BFS at every basin
sz = []
vis = set()
for x0, y0 in basin:
    if (x0, y0) in vis:
        continue
    vis.add((x0, y0))
    cur = 1
    queue = [(x0, y0)]
    for x, y in queue:
        for nx, ny in get_adjacent(x, y):
            if (nx, ny) in vis:
                continue
            # Ignore tiles that are 9
            # Also ignore tiles that are lower in value
            if 9 > grid[nx][ny] >= grid[x][y]:
                queue.append((nx, ny))
                cur += 1
                vis.add((nx, ny))
    sz.append(cur)

sz.sort(reverse=True)
print(total, sz[0] * sz[1] * sz[2])
