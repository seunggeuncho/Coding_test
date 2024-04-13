from collections import deque
import sys

sys.stdin = open('test.txt','r')
n,m = map(int, input().split())
dir = [[0,1],[1,0],[-1,0],[0,-1]]

miro = []
for _ in range(n):
    miro.append(list(input()))


def bfs(x,y,key):
    ans = 0
    check = [[0 for _ in range(n)] for _ in range(n)]
    que = deque([[x, y,0]])
    for _ in range(m - 1):
        que.append([x,y,0])
    while que:
        r,c,val = que.popleft()
        if [r,c] in key:
            key.pop(key.index([r,c]))
            ans += val
            if not key:
                return ans
        for idx in range(4):
            t_r = r + dir[idx][0]
            t_c = c + dir[idx][1]
            if 0<= t_r < n and 0 <= t_c < n:
                if miro[t_r][t_c] == 0 and check[t_r][t_c] == 0:
                    check[t_r][t_c] = 1
                    que.append([t_r,t_c,val + 1])
    return -1

key = []
s_loc = [0,0]
for r in range(len(miro)):
    for c in range(len(miro[0])):
        if miro[r][c] == 'S':
            s_loc[0] = r
            s_loc[1] = c
        elif miro[r][c] == 'K':
            key.append([r,c])
print(bfs(s_loc[0],s_loc[1],key))

