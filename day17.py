import re

def extract(line):
    return list(map(int, re.findall(r"-?\d+", line)))

X, Y = map(extract, open("inputs/day17.txt", "r").read().split(","))

def in_area(pos):
    return X[0] <= pos[0] <= X[1] and Y[0] <= pos[1] <= Y[1]

best = total = 0
for vy in range(-200, 200):
    for vx in range(0, 200):
        pos = [0, 0]
        v = [vx, vy]
        max_y = 0
        while pos[0] <= X[1] and Y[0] <= pos[1]:
            max_y = max(max_y, pos[1])
            if in_area(pos):
                best = max(best, max_y)
                total += 1
                break
            pos[0] += v[0]
            pos[1] += v[1]
            if v[0] > 0:
                v[0] -= 1
            v[1] -= 1
print(best, total)
