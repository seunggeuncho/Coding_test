import sys
dir = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]

sys.stdin = open('test.txt','r')
n = int(input())
mine = []
result = []
ans = [[] for _ in range(n)]
for _ in range(n):
    mine.append(list(input()))
for _ in range(n):
    result.append(list(input()))

def check_mine(x,y,lst):
    cnt = 0
    for i in range(8):
        tx = x + dir[i][0]
        ty = y + dir[i][1]
        if 0<= tx <n and 0<=ty <n and lst[tx][ty] == '*':
            cnt += 1
    return cnt
flag = 0
for r in range(n):
    for c in range(n):
        if result[r][c] == 'x' and mine[r][c] != '*':
            ans[r].append(str(check_mine(r,c,mine)))
        elif result[r][c] == '.':
            ans[r].append('.')
        elif result[r][c] == 'x' and mine[r][c] == '*':
            flag = 1
            ans[r].append('*')
if flag == 1:
    for r in range(n):
        for c in range(n):
            if mine[r][c] == '*':
                ans[r][c] = '*'
for i in range(n):
    for j in range(n):
        print(ans[i][j],end='')
    print()

"""
if flag == 1:
    for r in range(n):
        for c in range(n):
            if mine[r][c] == '*':
           """
