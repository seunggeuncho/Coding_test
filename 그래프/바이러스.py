import sys

sys.stdin = open('../sample2.txt', 'r')
computers = int(input())    #컴퓨터 개수
N = int(input())    #경로
visited = [0 for i in range(computers + 1)]
path = [[] for _ in range(computers + 1)]
for i in range(N):
    a,b = map(int, input().split())
    path[a].append(b)
    path[b].append(a)

def check(path, visited, cur):
    visited[cur] = 1
    for node in path[cur]:
        if visited[node] == 0:
            check(path, visited, node)
check(path, visited, 1)
print(visited.count(1) - 1)