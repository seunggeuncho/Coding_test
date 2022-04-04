def solution(n, computers):
    answer = 0
    visit = [0 for i in range(n)]
    def DFS(idx):
        if visit[idx] == 1:
            print(idx)
            nonlocal answer
            answer += 1
            return 
        else:
            visit[idx] = 1
            for num in range(n):
                if computers[idx][num] == 1 and idx != num:
                    DFS(num)
                    
    for idx in range(n):
        if visit[idx] == 0:
            DFS(idx)
    return answer
