import math
def solution(progresses, speeds):
    answer = []
    during = []
    for idx in range(len(progresses)):
        during.append(math.ceil((100 - progresses[idx]) / speeds[idx]))
    idx = 0
    while (idx < len(during)):
        pluse = 1
        if idx + pluse == len(during):
            answer.append(1)
            break
        while (during[idx] >= during[idx + pluse]):
            pluse += 1
            if idx + pluse == len(during):
                break
        answer.append(pluse)
        idx += pluse
    return answer
