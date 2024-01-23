import sys
from collections import deque
from copy import deepcopy

sys.stdin = open('test.txt','r')

n,m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
check = [-1 for _ in range(n + 1)]

for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

for idx in range(len(graph)):
    graph[idx].sort()

start, end = map(int, input().split())

que = deque([[start,0]])
check[start] = 0
while que:
    node,dis = que.popleft()
    if node == end:
        break
    for nxt in graph[node]:
        if check[nxt] == -1:
            check[nxt] = node
            que.append([nxt,dis + 1])

path = [end]
nxt = check[end]
while nxt != 0:
    path.append(nxt)
    nxt = check[nxt]
total = len(path) - 1
check = [-1 for _ in range(n + 1)]
for p in path:
    check[p] = 1
check[start] = -1
que = deque([[end,0]])
while que:
    node,dis = que.popleft()
    if node == start:
        break
    for nxt in graph[node]:
        if check[nxt] == -1:
            check[nxt] = 1
            que.append([nxt,dis + 1])
total += dis
print(total)