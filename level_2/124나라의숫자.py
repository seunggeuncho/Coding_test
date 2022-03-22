def solution(n):
    answer = []
    dic = {1:1, 2:2, 3:4}
    while (n >= 1):
        if n < 3:
            if n != 0:
                answer.append(dic[n])
            break
        else:
            num = int(n / 3)
            if n % 3 == 0:
                num -= 1
                answer.append(dic[3])
                n = num
            else:
                answer.append(dic[n % 3])
                n = num
    answer.reverse()
    answer = ''.join(map(str,answer))
    return answer
