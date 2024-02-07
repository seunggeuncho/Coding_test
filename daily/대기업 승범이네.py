import sys

sys.stdin = open('test.txt','r')

n = int(input())
graph = [[] for _ in range(n + 1)]
check = [0] * (n + 1)
tmp = list(map(int, input().split()))

for idx in range(len(tmp)):
    graph[tmp[idx]].append(idx + 2)

skill = [0]
skill += list(map(int, input().split()))

global ans
ans = 0


def dfs(start,total,cnt):
    print(start,total)
    if cnt == n:
        global ans
        ans = max(ans, total)
        return
    for ch in range(2):
        check[start] = ch
        if ch == 1:
            cnt += 1
        for val in graph[start]:
            if check[val] == 0:
                check[val] = 1
                if cnt % 2 == 1:
                    total += skill[start] * skill[val]
                    dfs(val, total, cnt + 1)
                    total -= skill[start] * skill[val]
                else:
                    dfs(val, total, cnt + 1)
                check[val] = 0
dfs(1,0,0)
print(ans)
