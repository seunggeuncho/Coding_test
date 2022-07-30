def divide(str):
    div = []
    for idx in range(len(str) - 1):
        tmp = str[idx:idx + 2]
        if tmp.isalpha():
            div.append(tmp.upper())
    return div
def solution(str1, str2):
    tmp1 = divide(str1)
    tmp2 = divide(str2)
    tmp2_tmp = tmp2.copy()
    tmp1_tmp = tmp1.copy()
    if not tmp1 and not tmp2:
        return 65536
    min = 0
    for tmp in tmp1:
        if tmp in tmp2_tmp:
            min += 1
            tmp2_tmp.remove(tmp)
    for idx in tmp2:
        if idx not in tmp1_tmp:
            tmp1.append(idx)
        else:
            tmp1_tmp.remove(idx)
    answer = min / len(tmp1) * 65536
    return math.trunc(answer)
