def solution(rows, columns, queries):
    answer = []
    lst = [[i + (columns * j) for i in range(1, columns + 1)] for j in range(0, rows)]
    print(lst)
    for x1,y1,x2,y2 in queries:
        temp = lst[x1 - 1][y1 - 1]
        mini = temp
        
        for idx in range(x1 - 1, x2 - 1):
            tmp = lst[idx + 1][y1 -1]
            lst[idx][y1 - 1] = tmp
            mini = min(tmp, mini)
        for idx in range(y1 - 1, y2 - 1):
            tmp = lst[x2 - 1][idx + 1]
            lst[x2 - 1][idx] = tmp
            mini = min(tmp, mini)
        for idx in range(x2 - 1, x1 - 1, -1):
            tmp = lst[idx - 1][y2 - 1]
            lst[idx][y2 -1]=tmp
            mini = min(tmp,mini)
        for idx in range(y2 -1, y1 - 1, -1):
            tmp = lst[x1 - 1][idx -1]
            lst[x1 - 1][idx] = tmp
            mini = min(mini, tmp)
        lst[x1 - 1][y1] = temp
        answer.append(mini)
    return answer
