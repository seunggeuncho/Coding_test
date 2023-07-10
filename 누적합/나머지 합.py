import sys

sys.stdin = open("test.txt",'r')

n,m = map(int, input().split())
lst = list(map(int,input().split()))
lst_len = len(lst)
ans = 0
for idx in range(1,lst_len):
    lst[idx] = lst[idx] + lst[idx -1]

for f in range(lst_len):
    if lst[f] % m == 0:
        ans += 1
    for n in range(f + 1,lst_len):
        if (lst[n] - lst[f]) % m == 0:
            ans += 1

print(ans)