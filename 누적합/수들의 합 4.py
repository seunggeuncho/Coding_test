import sys

sys.stdin = open("test",'r')
N,K = map(int, input().split())
lst = list(map(int, input().split()))
global answer
answer = 0

def check(idx):
    tmp = lst[:idx + 1]
    total = sum(tmp)
    global  answer
    if total == K:
        answer += 1
    for v in lst[idx + 1:]:
        total -= tmp.pop(0)
        tmp.append(v)
        total += v
        if total == K:
            answer += 1

for idx in range(0, N):
    check(idx)
print(answer)