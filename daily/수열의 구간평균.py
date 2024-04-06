import sys
from collections import defaultdict
sys.stdin = open('test.txt','r')

n,k = map(int, input().split())
lst = list(map(int, input().split()))

lst = [a - k for a in lst]

dic = defaultdict(int)
dic[0] = 1
pre_sum ,ans= 0,0

for l in lst:
    pre_sum += l

    ans += dic[pre_sum]
    dic[pre_sum] += 1
print(ans)

"""
answer = 0
for i in range(0,n):
    tmp = [0 for _ in range(n)]
    cnt = 1
    total  = lst[i]
    if total / cnt == k:
        answer+= 1
    for j in range(i + 1, n):
        total += lst[j]
        cnt += 1
        if total / cnt == k:
            answer += 1
"""
