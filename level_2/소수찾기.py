def decimal(num):
    if num < 2:
        return 0
    for i in range(2, num):
        if num % i == 0:
            return 0
    print(num)
    return 1
def solution(numbers):
    visit = [0 for i in range(len(numbers))]
    answer = 0
    numbers = list(numbers)
    lst = set()
    def DFS(word,k):
        if len(word) == k:
            if decimal(int(word)):
                nonlocal lst
                lst.add(int(word))
        for idx in range(len(numbers)):
            if visit[idx] == 0:
                visit[idx] = 1
                DFS(word + numbers[idx],k)
                visit[idx] = 0
    for i in range(1, len(numbers) + 1):
        DFS("",i)
    return len(lst)
