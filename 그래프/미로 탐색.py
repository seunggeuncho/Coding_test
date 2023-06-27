import sys
from collections import deque
sys.stdin = open("test.txt",'r')

miro = []
dir = [[0,1],[0,-1],[1,0],[-1,0]]
n,m = map(int, input().split(' '))
for _ in range(n):
    miro.append(list(map(int,input())))
def bfs():
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1
    que = deque([[0,0]])
    while que:
        x,y = que.popleft()
        for idx in range(4):
            dx = x + dir[idx][0]
            dy = y + dir[idx][1]
            if 0 <= dx < n and 0 <= dy < m:
                if visited[dx][dy] == 0 and miro[dx][dy] == 1:
                    que.append([dx,dy])
                    visited[dx][dy] = visited[x][y] + 1
    print(visited[n -1][m -1])
bfs()