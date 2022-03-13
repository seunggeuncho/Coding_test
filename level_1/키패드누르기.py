def dis(now, new):
    x = abs(now[0]-new[0])
    y = abs(now[1]-new[1])
    return x+y
def solution(numbers, hand):
    dic = {1:(1,1), 2:(1,2),3:(1,3),4:(2,1),5:(2,2),6:(2,3),7:(3,1),8:(3,2),9:(3,3),11:(4,1), 0:(4,2),12:(4,3)}
    answer=[]
    left = [1,4,7]
    right = [3,6,9]
    center = [2,5,8,0]
    now_left=10
    now_right=12
    if hand == "right":
        hand = "R"
    else:
        hand = "L"
    for num in numbers:
        if num in left:
            answer.append('L')
            now_left = num
        elif num in right:
            answer.append('R')
            now_right = num
        elif num in center:
            left_dis = dis(dic[num],dic[now_left])
            right_dis = dis(dic[num],dic[now_right])
            if right_dis > left_dis:
                answer.append('L')
                now_left=num
            elif right_dis < left_dis:
                answer.append('R')
                now_right=num
            elif right_dis == left_dis:
                answer.append(hand)
                if hand == "R":
                    now_right = num
                else:
                    now_left = num
    answer = ('').join(answer)
    return answer
