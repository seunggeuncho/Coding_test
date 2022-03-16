moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    answer =0
    bucket = []
    for select in moves:
        height = 0
        while (board[height][select - 1] == 0):
            height += 1
            print(height)
        bucket.append(board[height][select - 1])
        board[height][select - 1] = 0
    return answer
solution(board, moves)
