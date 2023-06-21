import sys
from heapq import heappop, heappush

sys.stdin = open("test.txt",'r')
n = int(input())
m = int(input())
parent = [i for i in range(n + 1)]
lst = []
for _ in range(m):
    s,e,d = map(int, input().split())
    heappush(lst, [d,s,e])

def check(a):
    if parent[a] != a:
        return check(parent[a])
    return a

def union(x,y):
    x = check(x)
    y = check(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
count = 0
while lst:
    dis, start, end = heappop(lst)
    if check(start) != check(end):
        count += dis
        union(start, end)
print(count)