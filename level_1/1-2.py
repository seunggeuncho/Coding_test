def order(num):
    return {
        6 : 1,
        5 : 2,
        4 : 3,
        3 : 4,
        2 : 5,
        1 : 6,
        0 : 6
    }.get(num, 6)

def solution(lottos,win_nums):
    answer=[]
    cnt = 0
    i = 0
    while i <len(lottos):
        j=0
        while j < len(win_nums):
            if win_nums[j] == lottos[i]:
                cnt+=1
            j+=1
        i+=1
    answer.append(order(cnt))
    i = 0
    while i <len(lottos):
        if lottos[i]==0:
            cnt+=1
        i+=1
    answer.append(order(cnt))
    answer.reverse()
    return answer
