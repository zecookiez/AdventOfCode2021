import re
from collections import Counter

def extract_int(line):
    return list(map(int, re.findall(r"\d+", line)))

input = open("inputs/day07.txt", "r").read()

"""
    The original complete search approach to try every position took ~400ms
    To optimize the search:
        Observe that both distance metric for Part 1 and 2 are convex
        The sum of multiple convex functions is convex
    And it just happens that we can apply unimodal search techniques to optimize this :P
    
    Ternary search is one way to do this, which lets us locate the minimum in O(log(M) * N) time where
        M = range of coordinates
        N = number of crabs
    You can additionally note that ~1/3 of the array is filled with duplicates, and thus we can group these crabs together
    
    Combining both results, the runtime reduces down to 7ms from 400ms.
"""

crabs = Counter(extract_int(input))

# Distance metrics used for Part 1 and 2
def dist_1(a, b):
    return abs(a - b)
def dist_2(a, b):
    diff = abs(a - b)
    return diff * (diff + 1) // 2

# Evaluate the minimum cost at that position
def cost(pos, crabs, metric):
    return sum(metric(pos, crab) * cnt for crab, cnt in crabs.items())

# Ternary search
def find_min(crabs, metric):
    left = min(crabs)
    right = max(crabs) + 1
    while right - left > 2:
        mid_1 = left + (right - left) // 3
        mid_2 = right - (right - left) // 3
        if cost(mid_1, crabs, metric) < cost(mid_2, crabs, metric):
            right = mid_2
        else:
            left = mid_1
    return min(cost(pos, crabs, metric) for pos in range(left, right + 1))

print(find_min(crabs, dist_1))
print(find_min(crabs, dist_2))
