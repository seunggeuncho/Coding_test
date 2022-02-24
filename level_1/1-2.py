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

////////////////////////////////////////////////////////////////////////(참고 풀이)
"""count 함수 사용하여 0의 개수를 세고 rank라는 배열을 만들어 개수에 따라 순위를 반환 받기"""



def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)  
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
