import sys

sys.stdin = open("test.txt",'r')
n, x = map(int, input().split())
lst = list(map(int, input().split()))

for i in range(1, len(lst)):
    lst[i] = lst[i] + lst[i - 1]
lst = [0] + lst
ans = 0
cnt = 0
for i in range(x, len(lst)):
    if ans < lst[i] - lst[i - x]:
        ans = lst[i] - lst[i - x]
        cnt = 0
        cnt += 1
    elif ans == lst[i] - lst[i - x]:
        cnt += 1
if ans == 0:
    print("SAD")
else:
    print(ans)
    print(cnt)