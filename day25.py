input = open("inputs/day25.txt", "r").readlines()

# Input parsing
east = set()
south = set()
R = len(input)
C = len(input[0].strip())
for i, line in enumerate(input):
    for j, ch in enumerate(line):
        if ch == ">":
            east.add((i, j))
        elif ch == "v":
            south.add((i, j))

def nxt(east, south):
    occ = east | south
    # Move east
    EAST = set()
    SOUTH = set()
    good = False
    for i, j in east:
        J = (j + 1) % C
        if (i, J) not in occ:
            EAST.add((i, J))
            good = True
        else:
            EAST.add((i, j))
    # Move south
    occ = EAST | south
    for i, j in south:
        I = (i + 1) % R
        if (I, j) not in occ:
            SOUTH.add((I, j))
            good = True
        else:
            SOUTH.add((i, j))
    return EAST, SOUTH, good

# Keep updating until nothing changes
step = 1
while True:
    east, south, changed = nxt(east, south)
    if not changed:
        print(step)
        break
    step += 1

