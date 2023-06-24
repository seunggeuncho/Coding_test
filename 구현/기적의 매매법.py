import sys

sys.stdin = open("test.txt",'r')
cash = int(input())
lst = list(map(int,input().split()))


def june():
    june_cnt = 0
    june_cash = cash
    for i in range(len(lst)):
        if june_cash == 0:
            break
        tmp = cash // lst[i]
        june_cnt += tmp
        june_cash -= lst[i] * tmp
    return june_cash + june_cnt * lst[-1]


def min():
    min_cnt = 0
    min_cash = cash
    increase = 0
    decrease = 0
    min_cnt = 0
    min_cash = cash
    for i in range(1, len(lst)):
        if lst[i] - lst[i - 1] < 0:
            decrease += 1
            increase = 0
        elif lst[i] - lst[i - 1] > 0:
            increase += 1
            decrease = 0
        else:
            increase = 0
            decrease = 0
        if increase >= 3:
            min_cash += min_cnt * lst[i]
            min_cnt = 0
            continue
        if decrease >= 3:
            tmp = min_cash // lst[i]
            min_cnt += tmp
            min_cash -= lst[i] * tmp

    return min_cnt * lst[-1] + min_cash

if june() > min():
    print("BNP")
elif june() < min():
    print("TIMING")
else:
    print("SAMESAME")


