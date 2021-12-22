
input = open("inputs/day18.txt", "r").readlines()

"""
This problem single-handedly made me spend 3 days trying to clean up the code
Approach:
    - Flatten the list into (element, depth) pairs
    - For explode the previous element will always be an integer
    - For split we can insert a new element at the specified index
    - For magnitude we need to manually combine elements from the highest level first
"""

def explode(fish):
    for ind, (el, dep) in enumerate(fish):
        if dep >= 4:
            # Add to the left element
            if ind != 0:
                fish[ind - 1] = el + fish[ind - 1][0], fish[ind - 1][1]
            # Add to the right element
            if ind + 2 < len(fish):
                fish[ind + 2] = fish[ind + 1][0] + fish[ind + 2][0], fish[ind + 2][1]
            # Deal with current element
            fish[ind] = 0, dep - 1
            if ind + 1 < len(fish):
                del fish[ind + 1]
            return fish, True
    return fish, False

def split(fish):
    for ind, (el, dep) in enumerate(fish):
        if el >= 10:
            # Create and update new elements
            fish[ind] = el // 2, dep + 1
            fish.insert(ind + 1, ((el + 1) // 2, dep + 1))
            return fish, True
    return fish, False

def add(fishA, fishB):
    # Combine both first
    res = [(el, dep + 1) for el, dep in fishA]
    res.extend([(el, dep + 1) for el, dep in fishB])
    while True:
        # Repeatedly explode
        res, verdict = explode(res)
        if verdict:
            continue
        # Repeatedly split
        res, verdict = split(res)
        if not verdict:
            break
    return res

def convert(fish, depth = 0):
    # Recursively flatten the list
    res = []
    for el in fish:
        if type(el) == list:
            res.extend(convert(el, depth + 1))
        else:
            res.append((el, depth))
    return res

def magnitude(fish):
    # Start combining from the highest depth first
    for lvl in range(3, 0, -1):
        for ind in range(len(fish)):
            if fish[ind][1] == lvl:
                # Combine left and right (ind and ind + 1)
                fish[ind] = fish[ind][0] * 3 + fish[ind + 1][0] * 2, lvl - 1
                fish[ind + 1] = -1, -1
        # Clean up the list
        fish = [(el, depth) for el, depth in fish if depth != -1]
    return fish[0][0] * 3 + fish[1][0] * 2

# Parse input
input = [*map(convert, map(eval, input))]

# Part 1
cur = input[0]
for line in input[1:]:
    cur = add(cur, line)
print(magnitude(cur))

# Part 2
print(max(magnitude(add(A, B)) for A in input for B in input))
