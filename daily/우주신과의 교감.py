import sys
import math

sys.stdin = open('test.txt','r')

n, m = map(int, input().split())

parent = [i for i in range(n + 1)]
check = [0] * (n + 1)
graph = []
answer = 0

for idx in range(n):
    x,y = map(int, input().split())
    graph.append([x,y,idx])
graph.sort(key = lambda x : (x[0],x[1]))

def dis(x1,y1,x2,y2):
    return math.sqrt(abs(x1 - x2) ** 2 +  abs(y1 - y2) ** 2)

def find(x, parent):
    if x != parent[x]:
        return find(parent[x],parent)
    return x

def union(x,y,parent):
    find_x = find(x)
    find_y = find(y)

    if find_x != find_y:
        if find_x < find_y:
            parent[find_y] = find_x
        else:
            parent[find_x] = find_y


for _ in range(m):
    n1,n2 = map(int, input().split())
    check[n1] = 1
    check[n2] = 1

for idx in range(len(graph) - 1):   #다음 노드와 비교해서 union
    x,y,node = graph[idx][0],graph[idx][1],graph[idx][2]

    if check[node] == 1:
        continue

