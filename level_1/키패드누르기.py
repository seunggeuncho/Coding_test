def solution(numbers, hand):
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
            if num == 0:
                num = 11
            if now_left + 2 == now_right:
                answer.append(hand)
                if hand == "R":
                    now_right = num
                else:
                    now_left = num
            elif abs(now_left - num) > abs(now_right - num):
                answer.append("R")
                now_right = num
            else:
                answer.append("L")
                now_left = num
            
    answer = ('').join(answer)
    return answer
