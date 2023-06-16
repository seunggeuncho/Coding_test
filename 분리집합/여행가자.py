import sys

sys.stdin = open('test.txt','r')
N = int(input())
M = int(input())

check_lst = [i for i in range(N + 1)]

def check(a):
    if check_lst[a] != a:
        check_lst[a] = check(check_lst[a])
    return check_lst[a]

def union(a, b):
    a = check(a)
    b = check(b)
    if a < b:
        check_lst[b] = a
    else:
        check_lst[a] = b
"""
for i in range(N):
    link = list(map(int, input().split()))
    for j in range(N):
        if link[j] == 1:
            union(i,j)
check_lst = [-1] + check_lst
path = list(map(int, input().split()))
start = check_lst[path[0]]
for i in range(1,M):
    if check_lst[path[i]] != start:
        print("NO")
        break
else:
    print("YES")
"""
for r in range(1,N + 1):
    lst = list(map(int, input().split()))
    for c in range(len(lst)):
        if lst[c] == 1:
            union(r,c + 1)

fin_lst = list(map(int, input().split()))

std = check_lst[fin_lst[0]]
for idx in range(1, len(fin_lst)):
    if std != check_lst[fin_lst[idx]]:
        print("NO")
        break
else:
    print("YES")