import sys
from collections import deque
from collections import defaultdict
sys.stdin = open("../sample2.txt", 'r')
N,M,V = map(int, input().split())
nodes = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)
for node in nodes:
    node.sort()

visited1 = [0 for _ in range(len(nodes))]
def DFS(nodes, start):
    visited1[start] = 1
    print(start, end=" ")
    for next in nodes[start]:
        if visited1[next] == 0:
            DFS(nodes, next)

DFS(nodes, V)
print()

def BFS(nodes, start):
    q = deque([start])
    visited = [0 for _ in range(len(nodes))]
    visited[start] = 1
    while q:
        cur = q.popleft()
        print(cur,end=" ")
        for next in nodes[cur]:
            if visited[next] == 0:
                visited[next] = 1
                q.append(next)

BFS(nodes, V)