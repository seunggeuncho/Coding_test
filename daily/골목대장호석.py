import sys
from collections import deque

""""
https://www.acmicpc.net/problem/20168
"""

sys.stdin = open('test.txt','r')

n,m,a,b,c = map(int,input().split())
graph = [[] for _ in range(n + 1)]
check = [0] * (n + 1)
check[a] = -1
for _ in range(m):
    s,e,cost = map(int,input().split())
    graph[s].append([e,cost])
    graph[e].append([s,cost])

for idx in range(n + 1):
    graph[idx].sort(key = lambda x : x[1])

def solv():
    que = deque([[a,c,0]])
    destin = float('inf')
    while que:
        node, cost, total = que.popleft()
        if node == b:
            destin = min(destin,total)
            continue
        for new_n, new_c in graph[node]:
            if cost - new_c < 0:
                continue
            if check[new_n] == 0 or new_n == b:
                check[new_n] = 1
                que.append([new_n,cost - new_c,max(total, new_c)])
    return destin

answer = solv()
if  answer != float('inf'):
    print(answer)
else:
    print(-1)