from collections import defaultdict
import queue
def solution(n, edge):
    node_dict = defaultdict(list)
    for node in edge:
            node_dict[node[0]].append(node[1])
            node_dict[node[1]].append(node[0])
    print(node_dict)
    dis = {node:float('inf') for node in range(1, n + 1)}
    print(dis)
    dis[1] = 0
    queue = []
    heapq.heappush(queue,[dis[1] , 1])
    answer = 0
    return answer
