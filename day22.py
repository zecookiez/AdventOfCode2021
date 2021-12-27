import re

def extract(line):
    return list(map(int, re.findall(r"-?\d+", line)))

input = open("inputs/day22.txt", "r").readlines()

arr = []
cube = [0] * 10**6
x_vals = []
for id, line in enumerate(input):
    xl, xr, yl, yr, zl, zr = extract(line)
    state = "on" in line
    arr.append((xl, xr, yl, yr, zl, zr, pow(2, id) if state else -pow(2, id)))
    x_vals.append(xl)
    x_vals.append(xr + 1)
    # Update bounds for part 1
    xl, xr = max(-50, xl), min(50, xr)
    yl, yr = max(-50, yl), min(50, yr)
    zl, zr = max(-50, zl), min(50, zr)
    if zl < zr:
        for x in range(xl + 50, xr + 51):
            x *= 10**4
            for y in range(yl + 50, yr + 51):
                y = y * 100 + x
                cube[y + zl:y + zr + 1] = [state] * (zr - zl + 1)

# Solve the 2D variant of the problem, which is almost identical to https://dmoj.ca/problem/ccc14s4
def solve(rects):
    # Coordinate compression + Line sweep
    events = []
    y_val = []
    for x1, y1, x2, y2, f in rects:
        # Build the line sweep events
        events.append((x1, y1, y2, f))
        events.append((x2, y1, y2, -f))
        y_val.append(y1)
        y_val.append(y2)
    events.sort()
    # Coordinate compress the y-values
    y_val = sorted(set(y_val))
    y_id = {val: ind for ind, val in enumerate(y_val)}
    state = [0] * len(y_id)
    tot = 0
    for ind, (x1, y1, y2, f) in enumerate(events):
        # Go through all y values and find the ones that are lit up
        # These are actually "rectangles"
        for y in range(len(y_val) - 1):
            if state[y] > 0:
                # Add rectangle area to total
                tot += (y_val[y + 1] - y_val[y]) * (x1 - events[ind - 1][0])
        # Update the rectangle states
        for y in range(y_id[y1], y_id[y2]):
            state[y] += f
    return tot

# Utility function to check if two intervals intersect
def intersects(L, R, xl, xr):
    return (xl <= L <= xr) or (xl <= R - 1 <= xr)

tot = 0
x_vals = sorted(set(x_vals))
for L, R in zip(x_vals, x_vals[1:]):
    # Solve for [L, R)
    cur = []
    for xl, xr, yl, yr, zl, zr, val in arr:
        # Add if [L, R) intersects with [xl, xr]
        if intersects(L, R, xl, xr):
            cur.append((yl, zl, yr + 1, zr + 1, val))
    tot += (R - L) * solve(cur)

print(sum(cube), tot)