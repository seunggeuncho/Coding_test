import sys

sys.stdin = open('test.txt','r')

n, m, k = map(int, input().split())

power = list(map(int, input().split()))

graph = []
parent = [i for i in range(n + 1)]

for p in power:
    parent[p] = 0

for _ in range(m):
    u,v,w = map(int, input().split())
    graph.append([w,u,v])
graph.sort()

def find(parent, node):
    if parent[node] != node:
        return find(parent, parent[node])
    return node

def union(parent,u,v):
    parent_u = find(parent, u)
    parent_v = find(parent, v)
    if parent_u < parent_v:
        parent[parent_v] = parent_u
    else:
        parent[parent_u] = parent_v

answer = 0
for w,u,v in graph:
    if find(parent, u) != find(parent,v):
        union(parent,u,v)
        answer += w
    if sum(parent) == 0:
        break
print(answer)