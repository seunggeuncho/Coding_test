def solution(clothes):
    answer = 1
    dic = {}
    num_dic = {}
    for cloth in clothes:
        print(cloth[1])
        if cloth[1] in dic.keys():
            num_dic[cloth[1]] += 1
        else:
            num_dic[cloth[1]] = 1
            dic[cloth[1]] = cloth[0]
    for case in num_dic.values():
        answer *= (case + 1)
    return answer - 1
