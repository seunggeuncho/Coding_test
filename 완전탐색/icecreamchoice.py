import sys
from itertools import combinations

sys.stdin = open('../sample2.txt', 'r')
N,M = map(int, input().split())
"""
bad = []
ice = [i for i in range(1, N + 1)]
for _ in range(M):
    bad.append(list(map(int, input().split())))

ans = 0
for per in combinations(ice, 3):
    check = 0
    for b in bad:
        print(per, b)
        if b[0] in per and b[1] in per:
            check = 1
            break
    if check == 0:
        ans += 1
print(ans)
"""
bad = []
for _ in range(M):
    bad.append(list(map(int, input().split())))
global ans
ans = 0
ice = [i for i in range(1, N + 1)]
def dfs(ice, bad, tmp, start):
    if len(tmp) == 2:
        for b in bad:
            if tmp[0] in b and tmp[1] in b:
                return
    if len(tmp) == 3:
        for b in bad:
            if (tmp[0] in b and tmp[2] in b) or (tmp[1] in b and tmp[2] in b):
                return
        print(tmp)
        global ans
        ans += 1
        return
    for idx in range(start, len(ice)):
        if len(tmp) != 0:
            if tmp[-1] >= ice[idx]:
                continue
        if ice[idx] not in tmp:
            tmp.append(ice[idx])
            dfs(ice, bad, tmp,start + 1)
            tmp.pop(-1)

dfs(ice, bad, [],0)
print(ans)