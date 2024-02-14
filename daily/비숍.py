import sys

sys.stdin = open('test.txt','r')

size = int(input())

chess = [list(map(int, input().split())) for _ in range(size)]

answer = 0


for row in range(size):
    for col in range(size):
        if chess[row][col] == 1:
            flag = 0
            for i in range(1,size):
                l_row, l_col = row - i, col - i
                r_row, r_col = row - i, col + i
                if 0 <= l_row < size and 0<= l_col < size:
                    if chess[l_row][l_col] == 2:
                        flag = 1
                if 0 <= r_row < size and 0 <= r_col < size:
                    if chess[r_row][r_col] == 2:
                        flag = 1
            if flag == 0:
                answer+= 1
                chess[row][col] = 2
print(chess)
print(answer)