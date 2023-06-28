import sys

n, k = map(int, input().split())
lst = list(map(str,input().split()))
ans = 0


def check(val):
    if len(val) <= len(str(n)) and val:
        global ans
        if int(''.join(val)) <= n:
           ans = max(ans, int(''.join(val)))
    if len(val) > len(str(n)):
        return
    for idx in lst:
        val.append(idx)
        check(val)
        val.pop(-1)
check([])
print(ans)