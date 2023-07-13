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

for idx in range(len(lst)):
    lst[idx] %= m
    if lst[idx] == 0:
        ans += 1
    dic[lst[idx]] += 1

for key, val in dic.items():
    ans += val * (val - 1) // 2

print(ans)