def solution(n, computers):    
    answer = 0
    visit = [0 for i in range(n)]
    for idx in range(n):
        if visit[idx] == 0:
            visit[idx] = 1
            DFS(idx)
    def DFS(idx):
        if computers[idx]
    return answer
