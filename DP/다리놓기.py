import sys

sys.stdin = open("test.txt",'r')
t = int(input())
dp = [[0 for _ in range(31)] for _ in range(31)]

for idx in range(1,31):
    dp[1][idx] = idx

for i in range(1, 31):
    for j in range(1, 31):
        for val in range(i-1, j):
            dp[i][j] += dp[i -1][val]

for _ in range(t):
    n, m = map(int, input().split())
    print(dp[n][m])
