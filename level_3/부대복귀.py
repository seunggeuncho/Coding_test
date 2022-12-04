import heapq
    
def solution(n, roads, sources, destination):
    g = [[] for _ in range(n + 1)]
    update = [float('inf') for _ in range(n + 1)]
    answer = []
    for road in roads:
        x, y = road
        g[x].append([1,y])
        g[y].append([1,x])
    hq = [(0, destination)]
    while hq:
        dis, cur_node = heapq.heappop(hq)
        if dis > update[cur_node]:
            continue
        update[cur_node] = dis
        for new_dis, new_node in g[cur_node]:
            dist = new_dis + dis
            if dist < update[new_node]:
                heapq.heappush(hq,(dist,new_node))
    
    for source in sources:
        if update[source] != float('inf'):
            answer.append(update[source])
        else:
            answer.append(-1)
    return answer
