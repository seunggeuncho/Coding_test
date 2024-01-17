import sys
from itertools import combinations

sys.stdin = open('test.txt','r')
n,m,k = map(int, input().split())

number = [i for i in range(1,n + 1)]
lst = []

for i in combinations(number, m):   #내가 뽑은 숫자
    lst.append(i)

total = len(lst) ** 2
cnt = 0

for choose in combinations(number, m):  #상대방이 뽑은 숫자
    mini = 0
    for c_lst in lst:
        for c_val in choose:
            if c_val in c_lst:
                mini += 1
                if mini >= k:
                    cnt += 1
                    break



print(cnt / total)

