import sys

sys.stdin = open('test.txt','r')

n, m, k = map(int, input().split())

power = list(map(int, input().split()))

graph = []
check = [0] * (n + 1)

for _ in range(m):
    u,v,w = map(int, input().split())
    graph.append([w,u,v])
    graph.sort()

answer = 0
for w,u,v in graph:
    if check[u] == 1 and check[v] == 1:
        continue
    else:
        print(w,u,v)
        check[u] = 1
        check[v] = 1
        answer += w
        if sum(check) == n:
            break
print(answer)
