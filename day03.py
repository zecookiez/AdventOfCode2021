input = open("inputs/day03.txt", "r").readlines()

nums = [line.strip() for line in input]

def count(pos, nums):
    cnt = [0, 0] # zero, one
    for num in nums:
        cnt[int(num[pos])] += 1
    return cnt

gamma = epsilon = 0
oxygen = nums[:]
carbon = nums[:]

WIDTH = len(nums[0])
for pos in range(WIDTH):
    # Part 1
    zero, one = count(pos, nums)
    gamma = gamma * 2 + (one > zero)
    epsilon = epsilon * 2 + (zero >= one)
    # (Part 2) Filter oxygen
    if len(oxygen) > 1:
        zero, one = count(pos, oxygen)
        target = "01"[one >= zero]
        oxygen = [j for j in oxygen if j[pos] == target]
    # (Part 2) Filter carbon
    if len(carbon) > 1:
        zero, one = count(pos, carbon)
        target = "10"[one >= zero]
        carbon = [j for j in carbon if j[pos] == target]

print(gamma * epsilon, int(oxygen[0], 2) * int(carbon[0], 2))
