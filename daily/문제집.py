import sys
from heapq import heappop, heappush

"""
백준 1766번
"""
sys.stdin = open('test.txt','r')

n,m = map(int, input().split())

check = [0] * (n + 1)
graph = [[] for _ in range((n + 1))]


for _ in range(m):
    a,b = map(int, input().split())
    check[b] += 1
    graph[a].append(b)

que = []

for idx in range(1, n + 1):
    if check[idx] == 0:
        heappush(que, idx)
answer = []
while que:
    val = heappop(que)
    answer.append(val)
    for i in graph[val]:
        check[i] -= 1
        if check[i] == 0:
            heappush(que,i)

print(*answer)