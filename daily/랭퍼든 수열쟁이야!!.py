import sys
import copy
sys.stdin = open('test.txt','r')

n,x,y = map(int, input().split())


total = []
check = []
for i in range(1, n + 1):
    check.append(i)
lst = [0] * (2 * n + 1)
lst[x] = lst[y] = y - x - 1

global ans
ans = 0

def dfs(depth):
    if depth == y - x - 1:
        dfs(depth + 1)

    if depth == n + 1:
        global ans
        ans += 1
        return
    for i in range(1, n + 1 - depth + 1):
        if lst[i] == lst[i + depth] == 0:
            lst[i] = lst[i + depth + 1] = i
            dfs(depth + 1)
            lst[i] = lst[i + depth + 1] = 0

dfs(1)
print(ans)