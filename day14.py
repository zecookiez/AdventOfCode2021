import re
from collections import Counter, defaultdict

def extract(line):
    return re.findall(r"[a-zA-Z]+", line)

template, rule = open("inputs/day14.txt", "r").read().split("\n\n")

rules = dict(map(extract, rule.strip().split("\n")))

def find_range(rounds):
    # Count initial pairs
    freq = Counter(zip(template, template[1:]))
    for _ in range(rounds):
        nxt = defaultdict(int)
        for pair, cnt in freq.items():
            # Check for insertion rules
            pair = "".join(pair)
            if pair in rules:
                left, mid, right = pair[0], rules[pair], pair[1]
                # Update adjacent pairs
                nxt[left, mid] += cnt
                nxt[mid, right] += cnt
            else:
                # No new pairs
                nxt[pair[0], pair[1]] += cnt
        freq = dict(nxt)
    # Count number of times every character appears
    result = defaultdict(int)
    for pair, cnt in freq.items():
        # If we only add the first element of each pair then every character is accounted for
        # (except for the last character in the final string)
        result[pair[0]] += cnt

    # Observation: the last element in the string is always template[-1]
    #              because every new insertion is *between* two old characters
    result[template[-1]] += 1
    result = result.values()
    return max(result) - min(result)

print(find_range(10), find_range(40))
