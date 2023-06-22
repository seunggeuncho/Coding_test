import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("test.txt",'r')
n = int(input())
"""
ans = float('inf')

def dfs(val,cnt):
    if val == n:
        global ans
        ans = min(ans, cnt)
        return
    for i in range(2,6,3):
        if val + i <= n:
            dfs(val + i, cnt + 1)
dfs(0,0)
if ans == float('inf'):
    print(-1)
print(ans)
"""
cnt = 0
while 1:
    if n % 5 == 0:
        cnt += n // 5
        break
    else:
        n -= 2
        cnt += 1
    if n < 0:
        break
if n < 0:
    print(-1)
else:
    print(cnt)