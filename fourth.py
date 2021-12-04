import re

# File Reading
with open("inputs/4", "r") as file:
    lines = file.read().splitlines()
drawn_nums = [int(s) for s in re.findall(r'\d+', lines[0])]
boards = []
boardtmp = []
for line in lines[2:]:
    if line == '':
        boards.append(boardtmp)
        boardtmp = []
    else:
        boardtmp.append([[int(s), False] for s in re.findall(r'\d+', line)])

boards.append(boardtmp)


def get_sum_board(board):
    counter = 0
    for r in range(5):
        for i in range(5):
            if board[r][i][1] is False:
                counter += board[r][i][0]
    return counter

def iterate_bingo():
    bb = set([i for i in range(len(boards))])
    for num in drawn_nums:
        for i, board in enumerate(boards):
            for r in range(5):
                for c in range(5):
                    if board[r][c][0] == num:
                        board[r][c][1] = True
                        if all(board[r][j][1] is True for j in range(5)):
                            if i in bb:
                                bb.remove(i)
                            if len(bb) == 0:
                                return get_sum_board(board) * num
                        if all(board[j][c][1] is True for j in range(5)):
                            if i in bb:
                                bb.remove(i)
                            if len(bb) == 0:
                                return get_sum_board(board) * num

current_num = iterate_bingo()

print(current_num)





print("")