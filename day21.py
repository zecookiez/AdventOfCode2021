import re
from itertools import product
from collections import Counter

def extract(line):
    return int(re.findall(r"\d+", line)[1]) - 1

original = p1, p2 = [extract(line) for line in open("inputs/day21.txt", "r").readlines()]

# The best dice roll function
roll = 0
def ROLL():
    global roll
    roll += 1
    return roll

# Part 1
p1s = p2s = 0
while True:
    A = ROLL() + ROLL() + ROLL()
    p1 = (p1 + A) % 10
    p1s += p1 + 1
    if p1s >= 1000:
        print(p2s * roll)
        break
    A = ROLL() + ROLL() + ROLL()
    p2 = (p2 + A) % 10
    p2s += p2 + 1
    if p2s >= 1000:
        print(p1s * roll)
        break

from itertools import product
# Memoize the recursive function :)
memo = {}
possible = Counter(map(sum, product([1, 2, 3], repeat=3)))
def helper(pos, score, turn):
    # Base cases
    if score[0] >= 21: return [1, 0]
    if score[1] >= 21: return [0, 1]
    # Memoization
    label = tuple(pos + score), turn
    if label in memo: return memo[label]
    # Otherwise try all possible dice outcomes
    res = [0, 0]
    for rolls, freq in possible.items():
        # Update position and score
        new_pos = pos[:]
        new_pos[turn] += rolls
        new_pos[turn] %= 10
        new_score = score[:]
        new_score[turn] += new_pos[turn] + 1
        # Count all universes
        out = helper(new_pos, new_score, turn ^ 1)
        # Combine results
        res[0] += out[0] * freq
        res[1] += out[1] * freq
    # Update memoization
    memo[label] = res
    return res
print(max(helper(original, [0, 0], 0)))
