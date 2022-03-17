moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    answer =0
    bucket = []
    for select in moves:
        height = 0
        while (board[height][select - 1] == 0 and height < len(board[0]) - 1):
            height += 1
        if (board[height][select - 1] != 0):
            bucket.append(board[height][select - 1])
            board[height][select - 1] = 0
        print(bucket)
    return answer
solution(board, moves)
