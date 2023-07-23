import sys

sys.stdin = open('test.txt','r')

n = int(input())
node = []
for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(n):
        if i < j:
            node.append([i,j,lst[j]])

node.sort(key = lambda x:x[2])

parent = [i for i in range(n)]

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

def union(x,y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
ans = 0
for x,y,val in node:
    if find(x) != find(y):
        union(x,y)
        ans += val
print(ans)