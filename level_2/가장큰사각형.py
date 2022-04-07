def check(idx, idx2, board):
    row = 0
    for num in range(idx2, len(board[idx])):
        if board[idx][num] == 1:
            row += 1
        else:
            break
    col = 0
    for num in range(idx, len(board)):
        if board[num][idx2] == 1:
            col += 1
        else:
            break
    for row in range(idx2, row):
        for col in range(idx, col):
            if board[col][row] != 1:
                if row == col:
                    return row * col
                elif row > col:
                    return col * col
                elif row < col:
                    return row * row
                     
def solution(board):
    answer = [0]
    for idx in range(len(board)):
        for idx2 in range(len(board[idx])):
            if board[idx][idx2] == 1:
                if check(idx, idx2,board) > answer[-1]:
                     answer.append(check(idx, idx2,board))
    print(answer)
    return max(answer)
