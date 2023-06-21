import sys
from collections import deque
sys.stdin = open("test.txt",'r')
n = int(input())
lst = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    a,b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
"""
def dfs(n):
    for val in lst[n]:
        if visited[val] == 0:
            visited[val] = n
            dfs(val)
dfs(1)
"""
q = deque([1])
while q:
    node = q.popleft()
    for val in lst[node]:
        if visited[val] == 0:
            visited[val] = node
            q.append(val)

print(*visited[2:], sep="\n")
