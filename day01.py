input = open("inputs/day01.txt", "r").readlines()

def part_1():
    prev = -1
    cnt = 0
    for line in input:
        cur = int(line[:-1])
        if cur > prev and prev != -1:
            cnt += 1
        prev = cur
    return cnt

def part_2():
    n1 = n2 = n3 = -1
    cnt = 0
    for line in input:
        cur = int(line[:-1])
        SUM = n1 + n2 + n3
        NEW = n2 + n3 + cur
        # Make sure the window has 3 numbers with min(...) > 0
        if NEW > SUM and min(n1, n2, n3) > 0:
            cnt += 1
        n1, n2, n3 = n2, n3, cur
    return cnt

# ~1ms using Python3.9
print(part_1(), part_2())