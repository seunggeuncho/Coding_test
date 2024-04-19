import sys

sys.stdin =open('test.txt','r')

n = int(input())
lst = list(map(int, input().split()))
oper = list(map(int, input().split()))
global min_val
global max_val

min_val = 1000000000
max_val = -1000000000

def plus(x,y):
    return x + y

def minus(x,y):
    return x - y

def divide(x,y):
    if 0 > x:
        return -(abs(x) // y)
    return x // y

def multiply(x,y):
    return x * y


def dfs(val, cnt):
    if cnt == n:
        global min_val
        global max_val
        min_val = min(min_val, val)
        max_val = max(max_val, val)
        return
    for idx in range(len(oper)):
        if oper[idx] >= 1:
            if idx == 0:
                tmp = plus(val, lst[cnt])
            elif idx == 1:
                tmp = minus(val, lst[cnt])
            elif idx == 2:
                tmp = multiply(val, lst[cnt])
            elif idx == 3:
                tmp = divide(val, lst[cnt])
            oper[idx] -=  1
            dfs(tmp, cnt + 1)
            oper[idx]  += 1
dfs(lst[0], 1)
print(max_val)
print(min_val)