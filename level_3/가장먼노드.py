import heapq

def solution(n, vertex):
    dic = defaultdict(list)
    for start, end in vertex:
        dic[start].append(end)
        dic[end].append(start)
    
    distance = [float('-inf')] * (n + 1)
    distance[1] = 0
    
    heap = []
    for node in dic[1]:
        distance[node] = 1
        heapq.heappush(heap, node)
    print(heap)
    while heap:
        now = heapq.heappop(heap)
        for node in dic[now]:
            if distance[node] == float('-inf') or distance[node] > distance[now] + 1:
                distance[node] = distance[now] + 1
                heapq.heappush(heap, node)
    
    max_distance = max(distance)
    count = 0
    for d in distance:
        if d == max_distance:
            count += 1
    
    return count
