from collections import defaultdict
orders=["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course=[2,3,4]
def solution(orders, course):
    def DFS(lst,order, num):
        nonlocal check
        print(lst)
        if len(lst) == num:
            nonlocal ords
            print(lst)
            lst =''.join(lst)
            if lst in ords:
                ords[lst] += 1
            else:
                ords[lst] = 1
        else:
            for idx in range(len(order)):
                if check[idx] == 0:
                    check[idx] = 1
                    lst.append(order[idx])
                    DFS(lst,order, num)
                    check[idx] = 0
                    lst.pop()
    for num in course:
        ords = dict()
        for order in orders:
            if len(order) >= num:
                check = [0 for i in range(len(order))]
                order = list(order)
                lst= []
                DFS(lst, order, num)
            
    answer = []
    return answer
solution(orders,course)
