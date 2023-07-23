import sys

sys.stdin = open('test.txt','r')

n = int(input())
lst = list(map(int, input().split()))
tree=[[] for _ in range(n)]

def Tree(tmp, r):
    mid = len(tmp) // 2
    tree[r].append(tmp[mid])
    if len(tmp) == 1:
        return
    Tree(tmp[:mid],r+1)
    Tree(tmp[mid+1:],r+1)

Tree(lst,0)
for i in range(n):
    print(*tree[i])