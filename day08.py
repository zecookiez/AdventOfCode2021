import re
from itertools import permutations

def extract(line):
    return re.findall(r"[a-z]+", line)

input = open("inputs/day08.txt", "r").readlines()

# Hardcode the segments needed for each digit
DIG = "abcefg cf acdeg acdfg bcdf abdfg abdefg acf abcdefg abcdfg"
DIG = {frozenset(key): str(ind) for ind, key in enumerate(DIG.split())}
total = 0
times = 0

# Utility function to map every character according to the permutation
def remap(perm, string):
    return frozenset(map(perm.get, string))

for line in input:
    lhs, rhs = map(extract, line.split("|"))
    # Part 1
    times += sum(len(dig) in [2, 3, 4, 7] for dig in rhs)
    # Part 2 (Try every permutation of the segments and see which one works)
    for perm in permutations("abcdefg"):
        mapping = dict(zip(perm, "abcdefg"))
        if all(remap(mapping, dig) in DIG for dig in lhs):
            total += int("".join(DIG[remap(mapping, dig)] for dig in rhs))
            break
print(times, total)
