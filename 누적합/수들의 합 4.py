import sys
from collections import defaultdict

sys.stdin = open("test",'r')
N,K = map(int, input().split())
lst = list(map(int, input().split()))
global answer
answer = 0

for i in range(1, len(lst)):
    lst[i] = lst[i - 1] + lst[i]

prefix = defaultdict(int)
for i in range(len(lst)):
    if lst[i] == K:
        answer += 1
    answer += prefix[lst[i] - K]
    prefix[lst[i]] += 1
    print(i, prefix, answer)
print(prefix)
print(answer)