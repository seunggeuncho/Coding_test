from collections import deque
import sys
import copy

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
    check = [[0 for _ in range(m + 2)] for _ in range(n + 2)]
    q = deque([[h1, h2,0]])
    check[h1][h2] = 1
    while q:
        x,y,val = q.popleft()
        if x == e1 and y == e2:
            return val
        for idx in range(4):
            changeX = x + dir[idx][0]
            changeY = y + dir[idx][1]
            if 1<= changeX <= n and 1<=changeY <= m:
                if lst[changeX][changeY] == 0 and check[changeX][changeY] == 0:
                    check[changeX][changeY] = 1
                    q.append([changeX, changeY, val + 1])

    return -1
result = bfs(lst)
if result != -1:
    ans = min(ans, result)

for r in range(n):
    for c in range(m):
        if lst[r][c] == 1:
            result = 0
            t_lst = copy.deepcopy(lst)
            t_lst[r][c] = 0
            result = bfs(t_lst)
            if result != -1:
                ans = min(ans, result)
if ans == float('inf'):
    print(-1)
else:
    print(ans)