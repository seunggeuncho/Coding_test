import sys

sys.stdin = open('test.txt','r')
N = int(input())
M = int(input())

check_lst = [i for i in range(N + 1)]

def check(a):
    if check_lst[a] != a:
        return check(check_lst[a])
    return a

def union(a, b):
    c_a = check(a)
    c_b = check(b)
    if c_a < c_b:
        check_lst[c_b] = c_a
    else:
        check_lst[c_a] = c_b

for r in range(1,N + 1):
    lst = list(map(int, input().split()))
    for c in range(len(lst)):
        if lst[c] == 1:
            union(r,c + 1)
            print(check_lst)

fin_lst = list(map(int, input().split()))

std = check_lst[fin_lst[0]]
for idx in range(1, len(fin_lst)):
    if std != check_lst[fin_lst[idx]]:
        print("NO")
        break
else:
    print("YES")