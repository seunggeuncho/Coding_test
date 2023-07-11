import sys
from collections import defaultdict

sys.stdin = open("test.txt",'r')

n,m = map(int, input().split())
lst = list(map(int,input().split()))
lst_len = len(lst)
dic = defaultdict(int)
ans = 0
for idx in range(1,lst_len):
    lst[idx] = lst[idx] + lst[idx -1]

for val in lst:
    if val % m == 0:
        ans += 1
    tmp = 1
    while val - tmp * m >= 0:
        ans += dic[val - tmp * m]
        tmp += 1
    dic[val] += 1

print(ans)