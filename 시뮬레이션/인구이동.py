import sys
from collections import deque
dir = [[1,0],[-1,0],[0,1],[0,-1]]

sys.stdin = open('../sample.txt', 'r')
n,l,r = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]


global info
info = 1


def bfs(i,j,check):
    global info

    q = deque([[i,j]])
    check[i][j] = 1
    tmp = [[i,j]]
    total = lst[i][j]
    while(q):

        row,col = q.popleft()
        for j in range(4):
            t_row = row + dir[j][0]
            t_col = col + dir[j][1]
            if 0 <= t_row < n and 0 <= t_col < n:
                if l <= abs(lst[row][col] - lst[t_row][t_col]) <= r and check[t_row][t_col] == 0:
                    check[t_row][t_col] = 1
                    q.append([t_row,t_col])
                    tmp.append([t_row,t_col])
                    total += lst[t_row][t_col]
    if len(tmp) >= 2:
        info = 1
    val = int(total / len(tmp))
    for va in tmp:
        x,y = va
        lst[x][y] = val


answer = 0
while (info == 1):
    info = 0
    check = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if check[i][j] == 0:
                bfs(i,j,check)
    if info == 1:
        answer += 1

print(answer)