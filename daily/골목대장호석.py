import sys
from collections import deque

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

def solv(s,t):
    que = deque([[s,0,t]])
    while que:
        node, cost, total = que.popleft()
        for new_n, new_c in graph[node]:

            big = new_c
            if new_c < check[node]:
                big = check[node]
            if new_n == b and total - new_c >= 0:
                if check[b] != 0 and check[b] > big:
                    check[b] = big
                elif check[b] == 0:
                    check[b] = big
            elif check[new_n] == 0 and total - new_c >= 0:
                check[new_n] = big
                que.append([new_n, new_c, total - new_c])
    return check

answer = solv(a,c)[b]
if  answer != 0:
    print(answer)
else:
    print(-1)