def solution(numbers, target):
    answer = 0
    lens = len(numbers)
    def dfs(num, result):
        if num == lens:
            if target == result:
                nonlocal answer
                answer += 1
            return 
        else:
            dfs(num + 1,result + numbers[num])
            dfs(num + 1,result - numbers[num])
    dfs(0,0)
    return answer
