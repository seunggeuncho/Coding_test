from collections import defaultdict
def solution(n, computers):
    edges = defaultdict(list)
    for idx in range(len(computers)):
        for idx2 in range(len(computers[idx])):
            if idx != idx2 and computers[idx][idx2] == 1:
                edges[idx].append(idx2)
    print(edges)
    answer = 0
    return answer
