
import sys

sys.stdin = open('test.txt','r')

n,m = map(int, input().split())

lst = set(input().split()[1:])

total_lst = []

for _ in range(m):
    total_lst.append(set(input().split()[1:]))

for _ in range(m):
    for party in total_lst:
        if party & lst:
            lst = lst.union(party)

cnt = 0
for lt in total_lst:
    if lt & lst:
        continue
    cnt += 1
print(cnt)
"""

import sys
sys.stdin = open('test.txt','r')
input = sys.stdin.readline

n, m = map(int, input().split())
knowList = set(input().split()[1:])
parties = []

for _ in range(m):
    parties.append(set(input().split()[1:]))

for _ in range(m):
    for party in parties:
        if party & knowList:
            knowList = knowList.union(party)
print(knowList)
cnt = 0
for party in parties:
    if party & knowList:
        continue
    cnt += 1

print(cnt)"""