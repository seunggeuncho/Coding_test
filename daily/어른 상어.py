import sys

sys.stdin = open('test.txt','r')

n,m,k = map(int, input().split())

lst = []

for _ in range(n):
    lst.append(list(map(int, input().split())))

now_dir = list(map(int, input().split()))
shark_dir = [[] for _ in range(m)]

for idx in range(m):
    for _ in range(4):
        shark_dir[idx].append(list(map(int, input().split())))

