rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

def solution(rows, columns, queries):
    answer = []
    lst = [[i + (columns * j) for i in range(1, rows + 1)] for j in range(0, columns)]
    for query in queries:
        temp = 0
        temp = lst[query[0]query[1]]
        for idx in range(query[1], query[3] + 1):
            print(idx)
    return answer
solution(rows, columns, queries)
