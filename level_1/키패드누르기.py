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
            tm_left = now_left
            tm_right = now_right
            if now_left in center:
                if now_left > num:
                    tm_left -= 2
                elif now_left < num:
                    tm_left += 2
            if now_right in center:
                if now_right > num:
                    tm_right -= 2
                elif now_right < num:
                    tm_right += 2
            if tm_left + 2 == tm_right or tm_left == tm_right:
                answer.append(hand)
                if hand == "R":
                    now_right = num
                else:
                    now_left = num
            elif abs(tm_left - num) > abs(tm_right - num):
                answer.append("R")
                now_right = num
            else:
                answer.append("L")
                now_left = num
            
    answer = ('').join(answer)
    return answer
