from collections import defaultdict
import sys
from collections import deque

sys.stdin = open('test.txt','r')
member = int(input())
lst = [[] for _ in range(member + 1)]
score = defaultdict(list)

minscore = float('inf')

while 1:
    tmp = list(map(int, input().split()))
    if tmp[0] == -1 and tmp[0] == -1:
        break
    lst[tmp[0]].append(tmp[1])
    lst[tmp[1]].append(tmp[0])


def bfs(n):
    que = deque([[n,0]])
    maxval = 0
    visited = [0] * (member + 1)
    visited[n] = 1
    while que:
        next, val = que.popleft()
        maxval = max(maxval, val)
        for idx in lst[next]:
            if visited[idx] == 0:
                visited[idx] = 1
                que.append([idx, val + 1])
    return maxval

for m in range(1, member + 1):
    val = bfs(m)
    minscore = min(minscore, val)
    score[val].append(m)

print(minscore, len(score[minscore]))
print(*score[minscore])

