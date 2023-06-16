import sys
sys.stdin = open("test.txt", 'r')

N,M = map(int, input().split())
lst = [i for i in range(N + 1)] #합집합 리스트
"""
def union(a,b): #작은 수로 합치기
    c_a = check(a)
    c_b = check(b)
    if c_a < c_b:
        lst[c_b] = c_a
    else:
        lst[c_a] = c_b

def check(a):
    if lst[a] != a:
        return check(lst[a])
    return a


for _ in range(M):
    std, a, b = map(int, input().split())
    if std == 0:
        union(a,b)
    else:
        if check(a) == check(b):
            print("YES")
        else:
            print("NO")
"""
def check(val):
    if lst[val] != val:
        return check(lst[val])
    return val

def union(a,b):
    c_a = check(a)
    c_b = check(b)
    if c_a < c_b:   #작은수로 합쳐진다
        lst[c_b] = c_a
    else:
        lst[c_a] = c_b

for _ in range(M):
    std, a, b = map(int, input().split())
    if std == 0:
        union(a,b)
    else:
        if check(a) == check(b):
            print("YES")
        else:
            print("NO")