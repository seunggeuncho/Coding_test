import sys
from collections import deque
sys.stdin = open('test.txt','r')
dir = [[0,1],[0,-1],[1,0],[-1,0]]

r,c = map(int,input().split())
vil = [list(input()) for _ in range(r)]
check = [[0 for _ in range(c)] for _ in range(r)]

global f_wolf
global f_sheep
f_wolf = 0
f_sheep = 0

def c_vil(row,col):
    q = deque([[row,col]])
    wolf = 0
    sheep = 0
    check[row][col] = 1
    while q:
        q_r,q_c = q.popleft()
        if vil[q_r][q_c] == 'v':
            wolf += 1
        elif vil[q_r][q_c] == 'k':
            sheep += 1
        for idx in range(4):
            t_r = q_r + dir[idx][0]
            t_c = q_c + dir[idx][1]
            if 0 <= t_r < r and 0 <= t_c < c:
                if vil[t_r][t_c] != '#' and check[t_r][t_c] == 0:
                    check[t_r][t_c] = 1
                    q.append([t_r,t_c])


    if wolf >= sheep:
        global f_wolf
        f_wolf += wolf
    else:
        global f_sheep
        f_sheep += sheep


for row in range(r):
    for col in range(c):
        if check[row][col] == 0 and vil[row][col] != '#':
            c_vil(row,col)
print(f_sheep,f_wolf)