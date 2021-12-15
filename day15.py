from heapq import heappop, heappush
input = open("inputs/day15.txt", "r").readlines()

init_grid = [] # Part 2 grid
p1_grid = []   # Part 1 grid
for line in input:
    line = list(map(int, line[:-1]))
    # Repeat the array 5 times horizontally with an offset every time
    real_line = []
    for add in range(5):
        real_line.extend([(val + add - 1) % 9 + 1 for val in line])
    init_grid.append(real_line)
    p1_grid.append(line)

# Repeat the grid 5 times vertically with an offset every time
grid = []
for add in range(5):
    for row in init_grid:
        grid.append([(val + add - 1) % 9 + 1 for val in row])

def path_find(grid):
    # Use Dijkstra's with a Priority Queue
    H = len(grid)
    W = len(grid[0])
    INF = 10**9
    best = [[INF] * W for _ in range(H)]
    queue = [(0, 0, 0)]
    while queue:
        dist, x, y = heappop(queue) # Retrieve lowest distance
        # Consider all four directions
        for nx, ny in (x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1):
            if 0 <= nx < H and 0 <= ny < W:
                # Only add to queue if new distance is better than what we have so far
                new_dist = dist + grid[nx][ny]
                if best[nx][ny] > new_dist:
                    best[nx][ny] = new_dist
                    heappush(queue, (new_dist, nx, ny))
    return best[-1][-1]

print(path_find(p1_grid), path_find(grid))
