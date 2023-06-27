import sys

sys.stdin = open("test.txt", 'r')
n = int(input())

lst = [0 for i in range(n)]
lst[0] = 1

for i in range(n):
    if lst[i] == 1:
        if i + 3 < n:
            lst[i + 3] = 2
        if i + 1 < n:
            lst[i + 1] = 2
    else:
        if i + 3 < n:
            lst[i + 3] = 1
        if i + 1 < n:
            lst[i + 1] = 1
if lst[-1] == 1:
    print("SK")
else:
    print("CY")