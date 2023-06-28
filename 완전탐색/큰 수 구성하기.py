import sys
sys.stdin = open("test.txt",'r')
n, k = map(int, input().split())
lst = list(map(str,input().split()))
ans = 0
def check(val):
    if len(val) == len(str(n)):
        global ans
        if int(''.join(val)) <= n:
           ans = max(ans, int(''.join(val)))
        return
    for idx in lst:
        val.append(idx)
        check(val)
        val.pop(-1)
check([])
print(ans)
