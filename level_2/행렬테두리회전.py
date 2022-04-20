    temp = []
    for idx in range(1,len(lst)):
        if idx == len(lst) - 1:
            temp.append(lst[0])
        temp.append(lst[idx])
    return temp
def solution(rows, columns, queries):
    answer = []
    lst = [[i + (columns * j) for i in range(1, rows + 1)] for j in range(0, columns)]
    for query in queries:
        temp = []
        left_row , left_col , right_row, right_col = query[0],query[1],query[2],query[3]
        for idx in range(left_row, right_row + 1):
            for idx2 in range(left_col, right_col + 1):
                if (idx >= left_row + 1 and idx <= right_row -1) and (idx2 >= left_col + 1 and idx2 <= right_col - 1):
                    continue
                temp.append(lst[idx - 1][idx2 - 1])
        answer.append(min(temp))
        print(temp)
        temp = re_list(temp)
        print(temp)
    return answer
