import sys
import heapq

sys.stdin = open('test','r')

n,m,k,x = map(int,input().split())
way = [[] for _ in range(n + 1)]
node = [float('inf') for _ in range(n + 1)] #node들의 거리 정보
for _ in range(m):
    start, end = list(map(int, input().split()))
    way[start].append(end)

lst = [[0,x]]
while lst:
    cur_dis, cur_node = heapq.heappop(lst)
    if node[cur_node] <= cur_dis:
        continue
    node[cur_node] = cur_dis
    for next_node in way[cur_node]:
        next_dis = 1 + node[cur_node]
        if next_dis < node[next_node]:
            heapq.heappush(lst, [next_dis, next_node])
check = 0
for idx in range(1, len(node)):
    if idx == x:
        continue
    if node[idx] == k:
        print(idx)
        check = 1
if check == 0:
    print(-1)
