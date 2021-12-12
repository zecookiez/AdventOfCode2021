from collections import defaultdict
input = open("inputs/day12.txt", "r").readlines()

# Build adjacency list
adj = defaultdict(list)
for line in input:
    node_1, node_2 = line[:-1].split("-")
    adj[node_1].append(node_2)
    adj[node_2].append(node_1)

# We can optimize this by adding memoization on the seen set
# The runtime without it isn't terrible,
# but it's a good place to shave time if I'm getting close to the 15s limit
def part_1(cur, seen):
    # If we've reached the end then we found a valid path
    if cur == "end":
        return 1
    # Otherwise go through the neighbors
    total = 0
    for nx in adj[cur]:
        if nx not in seen:
            # Add the lowercase variant into the visited set
            total += part_1(nx, seen | {nx.lower()})
    return total

# can_double is a boolean to keep track of whether we've visited a small cave twice
def part_2(cur, seen, can_double):
    # If we've reached the end then we found a valid path
    if cur == "end":
        return 1
    # Otherwise go through the neighbors
    total = 0
    for nx in adj[cur]:
        if nx == nx.lower():
            if nx not in seen:
                # Visiting normally
                total += part_2(nx, seen | {nx}, can_double)
            elif can_double and nx != "start":
                # Visiting twice condition
                total += part_2(nx, seen, False)
        else:
            # Visiting normally
            total += part_2(nx, seen, can_double)
    return total

print(part_1("start", {"start"}))
print(part_2("start", {"start"}, True))