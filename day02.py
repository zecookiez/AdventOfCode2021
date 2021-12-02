input = open("inputs/day02.txt", "r").readlines()

def part_1():
    X = depth = 0
    for line in input:
        command, x = line.split()
        if command == "forward":
            X += int(x)
        elif command == "down":
            depth += int(x)
        else:
            depth -= int(x)
    return X * depth

def part_2():
    X = depth = aim = 0
    for line in input:
        command, x = line.split()
        if command == "forward":
            X += int(x)
            depth += int(x) * aim
        elif command == "down":
            aim += int(x)
        else:
            aim -= int(x)
    return X * depth

# ~1ms using Python3.9
print(part_1(), part_2())