def equation(w, h, x):
    equation = -(h / w) * x + h
    return equation
def solution(w,h):
    total = w * h
    split_total = 0
    for x in range(w):
        diff = abs(equation(w, h, x) - equation(w, h, x + 1))
        if diff - int(diff) > 0:
            split_total += int(diff) + 1
        else:
            split_total += int(diff)
    answer = total - split_total
    return answer
