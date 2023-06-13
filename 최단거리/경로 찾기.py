import sys
from collections import deque
sys.stdin = open("test",'r')

N = int(input())
way = [[] for _ in range(N)]
for row in range(N):
    col = list(map(int, input().split()))
    for i in range(len(col)):
        if col[i] == 1:
            way[row].append(i)
lst = [[0 for _ in range(N)] for _ in range(N)]

def check(row):
    tmp = deque(way[row])
    while tmp:
        node = tmp.popleft()
        if lst[row][node] == 1:
            continue
        if node == row:
            lst[row][node] = 1
            continue
        lst[row][node] = 1
        for i in way[node]:
            tmp.append(i)

for r in range(N):
    check(r)
for i in range(N):
    for j in range(N):
        print(lst[i][j] ,end=" ")
    print()