import sys

sys.stdin = open("test",'r')
N,M = map(int, input().split())
lst = []
for r in range(N):
    lst.append(list(map(int, input().split())))

sum_lst = [[0 for _ in range(M + 1)]for _ in range(N + 1)]

for r in range(1, N + 1):
    for c in range(1,M + 1):
        sum_lst[r][c] = lst[r - 1][c - 1] + sum_lst[r - 1][c] + sum_lst[r][c - 1] - sum_lst[r - 1][c - 1]



ans = -float('inf')
for r in range(1,N + 1):
    for c in range(1, M + 1):
        for i in range(r, N + 1):
            for j in range(c, M + 1):
                ans = max(ans, sum_lst[i][j] - sum_lst[r - 1][j] - sum_lst[i][c - 1] + sum_lst[r - 1][c - 1])
print(ans)