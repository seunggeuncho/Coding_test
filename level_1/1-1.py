def solution(id_list, report, k):
    my_report = set(report)
    report = list(my_report)
    answer = [0 for i in range(len(id_list))]
    num = [0 for i in range (len(id_list))]
    for i in report:
        num[id_list.index(i.split(' ')[1])] += 1 
    for i in range (len(num)):
        if num[i] >= k:
            for j in report:
                if id_list[i] == j.split(' ')[1]:
                    answer[id_list.index(j.split(' ')[0])] += 1
    return answer