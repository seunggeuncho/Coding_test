import sys

sys.stdin = open('test.txt','r')
n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))
lst.sort(reverse=True)
ans = 0
for i in range(len(lst)):
    if lst[i] - (i+1 - 1) > 0:
        ans += lst[i] - (i+1 - 1)
print(ans)