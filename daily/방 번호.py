from copy import deepcopy
import sys

sys.stdin = open('test.txt','r')

n = int(input())
p = list(map(int, input().split()))
m = int(input())
min_val = min(p)






"""global ans
ans = 0

dp = [-float("inf") for _ in range(m+1)]
for i in range(n-1,-1,-1):
    tmp = p[i]
    for j in range(tmp, m+1):
        dp[j] = max(dp[j], i, dp[j-tmp]*10 + i)
print(dp)
print(dp[m])"""
"""
def dfs(lst, cnt,min_val):
    if cnt < min_val:
        global ans
        ans = max(ans,(int(''.join(map(str,lst)))))
        return
    for idx in range(n):
        if p[idx] <= cnt:
            cnt -= p[idx]
            lst.append(idx)
            dfs(deepcopy(lst), cnt,min_val)
            lst.pop()
            cnt += p[idx]
dfs([],m,min_val)
print(ans)"""