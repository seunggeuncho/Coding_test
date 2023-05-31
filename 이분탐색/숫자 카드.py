import sys

sys.stdin = open('sample.txt','r')
N = int(input())
N_card = list(map(int, input().split()))
M = int(input())
M_card = list(map(int, input().split()))
N_card.sort()

def check(m):
    left = 0
    right = N - 1
    while left <= right:
        middle = (left + right) // 2
        if N_card[middle] > m:
            right = middle - 1
        elif N_card[middle] < m:
            left = middle + 1
        elif N_card[middle] == m:
            print(1,end=' ')
            return
    print(0, end=' ')
    return
for m in M_card:
    check(m)