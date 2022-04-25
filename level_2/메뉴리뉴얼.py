    answer = []
    def DFS(lst,order, num,cmp):
        nonlocal check
        if len(lst) == num:
            nonlocal ords
            lsts = lst[:]
            lsts.sort()
            lsts =''.join(lsts)
            print(lst)
            if lsts in ords:
                ords[lsts] += 1
            else:
                ords[lsts] = 1
        else:
            for idx in range(len(order)):
                if check[idx] == 0 and cmp <= idx:
                    check[idx] = 1
                    lst.append(order[idx])
                    DFS(lst,order, num,idx)
                    check[idx] = 0
                    lst.pop()
    for num in course:
        ords = dict()
        for order in orders:
            if len(order) >= num:
                check = [0 for i in range(len(order))]
                order = list(order)
                lst= []
                DFS(lst, order, num , 0)
            print(ords)
        for k,v in ords.items():
             if max(ords.values()) == v and v > 1:
                answer.append(k)
    return answer
