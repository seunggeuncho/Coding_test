import sys
from collections import deque

sys.stdin = open('test.txt','r')
"""
n,start, end, info = map(int, input().split())
graph = [[] for _ in range(n)]
parent = [i for i in range(n)]

for _ in range(info):   #교통 정보
    s,e,charge = map(int, input().split())
    graph[s].append([e,-charge])

earn = list(map(int, input().split()))

for idx in range(len(graph)):
    for idx2 in range(len(graph[idx])):
        graph[idx][idx2][1] += earn[graph[idx][idx2][0]]
    graph[idx].sort(key = lambda x : x[1], reverse=True)

print(graph)
que = deque([[start,0]])

def check(node,parent):
    if node != parent[node]:
        return check(parent[node],parent)
    return node

def union(a,b,parent):
    new_a = check(a,parent)
    new_b = check(b,parent)
    if new_a < new_b:
        parent[new_b] = new_a
    else:
        parent[new_a] = new_b

possible = 0
node_check = [0] * n
node_check[0] = 1

total_cnt = 0
while que:
    node,ch = que.popleft()
    total_cnt += ch
    if node == end:
        possible = 1
        break
    for new, new_charge in graph[node]:
        if check(node,parent) != check(new,parent):
            union(node, new,parent)
        if node_check[new] == 0:
            node_check[new] = 1
            que.append([new, new_charge])
print(total_cnt)
print(possible)

"""
n,start, end, m = map(int, input().split())

info = []
for _ in range(m):
    s,e,f = list(map(int, input().split()))
    info.append([s,e,-f])

earn = list(map(int, input().split()))
for idx in range(len(info)):
    info[idx][2] += earn[info[idx][1]]

fee_info = [float('-INF')] * n

def bfs(node, end):
    que = deque([node])
    check = [0] * n
    check[node] = 1
    while que:
        node = que.popleft()
        if node == end:
            return True
        for now, nxt, charge in info:
            if now == node:
                if check[nxt] == 0:
                    check[nxt] = 1
                    que.append(nxt)
    return False


def bellman(s):
    fee_info[s] = earn[s]
    for i in range(n -1):
        for node, next_node ,c in info:
            if fee_info[node] != float('-INF') and fee_info[next_node] < fee_info[node] + c:
                fee_info[next_node] = fee_info[node] + c

    if fee_info[end] == float('-INF'):
        return 'gg'

    for s,e,c in info:
        if fee_info[s] != float('-INF') and fee_info[e] < fee_info[s] + c:
            if bfs(e,end):
                return "Gee"
    return fee_info[end]

print(bellman(start))