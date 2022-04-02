def decimal(num):
    if num < 2:
        return 0
    for i in range(2, num):
        if num % i == 0:
            return 0
    return 1
def solution(numbers):
    answer = 0
    numbers = list(numbers)
    num_li = []
    def DFS(idx , num_li):
        if idx > len(numbers):
            return
        else:
            nonlocal answer
            num = int(().join(num_li))
            answer += decimal(num)
        for i in range(len(numbers)):
            DFS(idx + 1,num_li.append(numbers[i]))
    DFS(0, num_li)
    return answer

