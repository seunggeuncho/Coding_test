from collections import deque
import sys


sys.stdin = open('test.txt','r')

n,m = map(int, input().split())
h1,h2 = map(int, input().split())
e1,e2 = map(int, input().split())
dir = [[0,1],[0,-1],[1,0],[-1,0]]

lst = [[0 for _ in range(m + 2)]]
for _ in range(n):
    t = [0] + list(map(int, input().split())) + [0]
    lst.append(t)

lst.append([0 for _ in range(m + 2)])

ans = float('inf')
def bfs(lst):
    check = [[[False for _ in range(2)] for _ in range(m + 2)] for _ in range(n + 2)]
    q = deque([[h1, h2,0,1]])
    check[h1][h2][1] = 1
    while q:
        print(q)
        x,y,val,flag = q.popleft()
        if x == e1 and y == e2:
            return val
        for idx in range(4):
            changeX = x + dir[idx][0]
            changeY = y + dir[idx][1]
            if 1<= changeX <= n and 1<=changeY <= m:
                if check[changeX][changeY][flag]:
                    continue
                elif lst[changeX][changeY] == 0:
                    check[changeX][changeY][flag] = 1
                    q.append([changeX, changeY, val + 1,flag])
                elif lst[changeX][changeY] == 1 and flag == 1:
                    check[changeX][changeY][0] = 1
                    q.append([changeX, changeY, val + 1, 0])
    return -1
print(bfs(lst))

