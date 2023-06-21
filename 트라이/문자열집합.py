import sys
from collections import defaultdict
sys.stdin = open("test.txt",'r')

n,m = map(int, input().split())
dic = defaultdict(int)
for _ in range(n):
    tmp = input()
    dic[tmp] += 1
cnt = 0
for _ in range(m):
    tmp = input()
    if tmp in dic:
        cnt += 1
print(cnt)