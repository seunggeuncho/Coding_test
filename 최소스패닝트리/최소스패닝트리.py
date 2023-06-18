import sys
from collections import deque

sys.stdin = open("test.txt",'r')
v,e = map(int, input().split())
lst = []
parent = [i for i in range(v + 1)]
ans = 0
for _ in range(e):
    start, end, dis = map(int, input().split())
    lst.append([start, end,dis])
lst.sort(key = lambda x : x[2])

def check(node):
    if parent[node] != node:
        return check(parent[node])
    return node

def union(x,y):
    a = check(x)
    b = check(y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in lst:
    start, end, dis = i
    if check(start) != check(end):
        union(start, end)
        ans += dis

print(ans)



"""
que = deque([[1,0]])
while que:
    node, dis = que.popleft()
    if dis >= dis_lst[node]:
        continue
    dis_lst[node] = dis
    for next, next_dis in lst[node]:
        total_dis = next_dis + dis
        if total_dis < dis_lst[next]:
            que.append([next,total_dis])
print(dis_lst)

graph = [[float('inf') for _ in range(v + 1)] for _ in range(v + 1)]
for i in range(v + 1):
    graph[i][i] = 0

for i in range(len(lst)):
    for val in lst[i]:
        end, dis = val
        graph[i][end] = dis

for i in range(v + 1):
    for j in range(v + 1):
        for k in range(v + 1):
            if graph[j][k] > graph[j][i] + graph[i][k]:
                graph[j][k] = graph[j][i] + graph[i][k]
"""