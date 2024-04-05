import sys
from collections import defaultdict
sys.stdin = open('test.txt','r')

n,k = map(int, input().split())
lst = list(map(int, input().split()))


sum_lst = [0 for _ in range(n)]
sum_lst[0] = lst[0]
for idx in range(1, n):
    sum_lst[idx] = lst[idx] + sum_lst[idx -1]

sum_lst = [0] + sum_lst
dic = defaultdict(int)
result = 0
for idx in range(1,n + 1):
    acc = sum_lst[idx] - idx * k

    result += dic[acc]
    dic[acc] += 1

print(result + dic[0])
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
