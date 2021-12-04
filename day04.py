import re

def extract_int(line):
    return list(map(int, re.findall(r"\d+", line)))

input = open("inputs/day04.txt", "r").read().split("\n\n")

# Input processing
order = extract_int(input[0])
boards = [
    [extract_int(line) for line in board.split("\n")] for board in input[1:]
]

def is_complete(board):
    if any(all(row) for row in board):
        return True
    return any(all(col) for col in zip(*board))

# Create a board of booleans for every bingo board
marked = [
    [[False] * 5 for i in range(5)] for _ in boards
]
final = -1
complete = set()
for num in order:
    # Update all bingo boards
    for ind, board in enumerate(boards):
        for x, row in enumerate(board):
            if num in row:
                pos = boards[ind][x].index(num)
                marked[ind][x][pos] = True
    # Identify winning boards
    for ind, (cur, board) in enumerate(zip(marked, boards)):
        # Ignore if board is complete
        if ind not in complete and is_complete(cur):
            complete.add(ind)
            # Calculate score
            score = num * sum(
                board[row][col] * (1 - cur[row][col]) for row in range(5) for col in range(5)
            )
            # First winning board (part 1)
            if final == -1:
                print(score)
            final = score
# Last winning board (part 2)
print(final)
