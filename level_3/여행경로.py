from collections import defaultdict
def solution(tickets):
    answer = []
    ticket = defaultdict(list)
    for tic in tickets:
            ticket[tic[0]].append(tic[1])
            ticket[tic[0]].sort()
    visited = ['ICN']
    def DFS(visited):
        if len(visited) == len(tickets) + 1:
            nonlocal answer
            if not answer:
                answer.extend(visited)

        if visited[-1] in ticket:
            if ticket[visited[-1]] is not None:
                    for idx in range(len(ticket[visited[-1]])):
                        tic = ticket[visited[-1]].pop(idx)
                        visited.append(tic)
                        DFS(visited)
                        visited.pop(-1)
                        ticket[visited[-1]].insert(0,tic)
    DFS(visited)
    return answer
