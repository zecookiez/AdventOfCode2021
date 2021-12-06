import re
from collections import defaultdict, Counter

def extract_int(line):
    return list(map(int, re.findall(r"\d+", line)))

input = open("inputs/day06.txt", "r").read()

# Key observation is that we can group the lanternfish by their internal timer values
# Thus, there are at most 9 distinct lanternfish groups (0 to 8 inclusive)

for days in 80, 256: # Part 1, Part 2
    state = Counter(extract_int(input))
    for _ in range(days):
        nx = defaultdict(int)
        for key, val in state.items():
            if key == 0:
                nx[6] += val
                nx[8] += val
            else:
                nx[key - 1] += val
        state = nx
    print(sum(state.values()))
