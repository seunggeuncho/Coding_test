import sys
from collections import deque
sys.stdin = open("test.txt",'r')
n, m = map(int, input().split())
way = [[] for _ in range(n + 1)]    #노드간의 간선
for _ in range(m):
    a, b = map(int, input().split())
    way[b].append(a)
def hacking(node):
    visited = [0] * (n + 1)
    que = deque([node])
    cnt = 0
    while que:
        cur = que.popleft()
        for val in way[cur]:
            if visited[val] == 0 and val != node:
                visited[val] = -1
                cnt += 1
                que.append(val)
    return cnt

maxcnt = 1
ans = []

for i in range(1, n+ 1):
    cnt = hacking(i)
    if maxcnt < cnt:
        maxcnt = cnt
        ans.clear()
        ans.append(i)
    elif maxcnt == cnt:
        ans.append(i)


print(*ans)