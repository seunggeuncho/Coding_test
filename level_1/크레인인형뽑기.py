    flag = 0
    num = 0
    while (flag == 0):
        for sort in range(len(bucket)):
            if sort == len(bucket) - 1:
                flag = 1
                break
            if bucket[sort] == bucket[sort + 1]:
                del bucket[sort]
                del bucket[sort]
                num = num + 2
                break
        print(bucket)
    return num
            
                
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
    answer = check(bucket)
    return answer
