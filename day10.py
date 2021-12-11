input = open("inputs/day10.txt", "r").readlines()

# Define constants
OPEN, CLOSE = "{(<[", "})>]"
values_1, values_2 = [1197, 3, 25137, 57], [3, 1, 4, 2]

# Build lookup tables
table_1 = dict(zip(CLOSE, values_1))
table_2 = dict(zip(CLOSE, values_2))
closed = dict(zip(OPEN, CLOSE))

# Final output
score, scores = 0, []

# Process input
for line in input:
    brackets = []
    for ch in line[:-1]:
        # Add to the stack of brackets if it is an opening bracket
        if ch in OPEN:
            brackets.append(closed[ch])
        # Check if matches last opening bracket
        elif brackets and brackets[-1] == ch:
            brackets.pop()
        else:
            # Corrupted line
            score += table_1[ch]
            break
    else:
        # Safe (but incomplete) line
        total = 0
        for ch in brackets[::-1]: # Reversed to imitate stack
            total = total * 5 + table_2[ch]
        scores.append(total)

# Output answers
scores.sort()
print(score)
print(scores[len(scores) // 2])
