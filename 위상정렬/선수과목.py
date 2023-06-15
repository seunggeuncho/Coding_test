import sys
from collections import deque

sys.stdin = open("test.txt",'r')

N,M = map(int, input().split())
lst = [[] for _ in range(N + 1)]
check = [0] * (N + 1)
answer = [0] * (N + 1)
for _ in range(M):
    start, end = map(int, input().split())
    check[end] += 1
    lst[start].append(end)
q = deque()
for i in range(1, len(check)):
    if check[i] == 0:
        answer[i] = 1
        q.append([i,2])

while q:
    now, count  = q.popleft()
    for next in lst[now]:
        check[next] -= 1
        if check[next] == 0:
            answer[next] = count
            q.append([next,count + 1])

print(*answer[1:])
