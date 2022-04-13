from collections import defaultdict
import heapq
def solution(n, edge):
    node_dict = defaultdict(list)
    for node in edge:
            node_dict[node[0]].append(node[1])
            node_dict[node[1]].append(node[0])
    print(node_dict)
    dis = {node:float('inf') for node in range(1, n + 1)}
    dis[1] = 0
    queue = []
    heapq.heappush(queue,[dis[1] , 1])
    while queue:
        current_dis,current_node = heapq.heappop(queue)
        if dis[current_node] < current_dis:
            continue
        
        for adjacent in node_dict[current_node]:
            distance = current_dis + 1
            if distance < dis[adjacent]:
                dis[adjacent] = distance
                heapq.heappush(queue,[adjacent])
    answer = 0
    return answer
