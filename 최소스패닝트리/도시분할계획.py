import sys

sys.stdin = open('test.txt','r')
n,m = map(int, input().split())
node= []
check = [0 for _ in range(n + 1)]
ans = 0
street = []
for _ in range(m):
    a,b,c = map(int, input().split())
    node.append([a,b,c])

node.sort(key=lambda x:x[2])
parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

for x, y, val in node:
    if find(x) != find(y):
        union(x,y)
        ans += val
        street.append(val)
ans -= street[-1]
print(ans)