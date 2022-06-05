input = """2 0 0 2
        4 16 8 2
        2 64 32 4
        1024 1024 64 0
        0"""

directions = {0: (-1, 0), 1: (0, -1), 2: (1, 0), 3: (0, 1)}


def getBoardAndDir():
    board = []
    for enum, line in enumerate(input.split("\n")):
        if enum < 4:
            newLine = []
            for num in line.split():
                newLine.append(int(num))
            board.append(newLine)
        else:
            dir = int(line.strip())

    return board, dir


board, dir = getBoardAndDir()

print(board)

for line in board:

