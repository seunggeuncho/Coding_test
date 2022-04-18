def solution(rows, columns, queries):
    lst = [[i + (columns * j) for i in range(1, rows + 1)] for j in range(0, columns)]
    for query in queries:
        temp = []
        left_row , left_col , right_row, right_col = query[0],query[1],query[2],query[3]
        for idx in range(left_row, right_row):
            for idx2 in range(left_col, right_col):
                if (idx == left_row or idx == right_row) and (idx2 == left_col or idx2 == right_col):
                    temp.append(query[idx][idx2])
    print(temp)
    answer = 0
    return answer
