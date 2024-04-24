from collections import defaultdict

edges=[[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
def solution(edges):
    answer = [0, 0, 0, 0]

    nodeCnt = defaultdict(list)
    for edge in edges:
        a = edge[0]
        b = edge[1]
        if not nodeCnt.get(a):
            nodeCnt[a] = [0,0]
        if not nodeCnt.get(b):
            nodeCnt[b] = [0,0]
        nodeCnt[a][0] += 1
        nodeCnt[b][1] += 1

    for key,val in nodeCnt.items():
        if val[0] >= 2 and val[1] == 0:
            answer[0] = key
        elif val[0] == 0 and val[1] > 0:
            answer[2] += 1
        elif val[0] >= 2 and val[1] >= 2:
            answer[3] += 1

    answer[1] = nodeCnt[answer[0]][0] - answer[2] - answer[3]
    return answer



print(solution(edges))