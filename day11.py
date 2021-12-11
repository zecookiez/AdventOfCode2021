input = open("inputs/day11.txt", "r").readlines()

# Parse input
SZ = 10
grid = [list(map(int, line[:-1])) for line in input]

# Utility function to obtain adjacent tiles
def adjacent(x, y):
    for dx in -1, 0, 1:
        for dy in -1, 0, 1:
            if dx == 0 == dy:
                continue
            if 0 <= x + dx < SZ and \
               0 <= y + dy < SZ:
                yield (x + dx, y + dy)

# Utility function to simulate a step
def simulate(grid):
    queue = []
    flashed = set() # Tracks all flashing octopuses
    # Increment all octopuses by 1
    for x in range(SZ):
        for y in range(SZ):
            grid[x][y] += 1
            if grid[x][y] > 9:
                queue.append((x, y))
                flashed.add((x, y))
    # BFS to flash the remaining octopuses
    for x, y in queue:
        for nx, ny in adjacent(x, y):
            grid[nx][ny] += 1
            if grid[nx][ny] > 9 and (nx, ny) not in flashed:
                queue.append((nx, ny))
                flashed.add((nx, ny))
    # Mark all flashed to 0
    for x, y in flashed:
        grid[x][y] = 0
    return len(flashed)


step = 1
count = []
while True:
    count.append(simulate(grid))
    if count[-1] == SZ * SZ:
        print(sum(count[:100]))
        print(step)
        break
    step += 1
