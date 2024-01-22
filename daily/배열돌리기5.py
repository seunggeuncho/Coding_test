import sys

sys.stdin = open('test.txt','r')

n,m, many = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
command = list(map(int, input().split()))


def updown(arr):    #1
    tmp = []
    for r in range(len(arr) - 1,-1,-1):
        tmp.append(arr[r])
    return tmp

def leftright(arr): #2
    tmp = []
    for r in range(len(arr)):
        tmp.append(arr[r][::-1])
    return tmp
"""
def spinright(arr): #3
    tmp = []
    for c in range(len(arr[0])):
        one_tmp = []
        for r in range(len(arr) - 1, -1, -1):
            one_tmp.append(arr[r][c])
        tmp.append(one_tmp)
    return tmp

def spinleft(arr):  #4
    tmp = []
    for c in range(len(arr[0]) - 1,-1,-1):
        one_tmp = []
        for r in range(len(arr)):
            one_tmp.append(arr[r][c])
        tmp.append(one_tmp)
    return tmp
"""
def spinright(arr): #3
    tmp = [[0 for _ in range()]]

def partspinright(arr): #5
    tmp = []
    part1 = []
    part2 = []
    part3 = []
    part4 = []
    row = len(arr)
    col = len(arr[0])
    for r in range(row // 2):
        part1.append(arr[r][:col//2])
        part2.append(arr[r][col//2:])
        part4.append(arr[r + row//2][:col//2])
        part3.append(arr[r + row//2][col//2:])

    for sum_up in range(row // 2):
        tmp.append(part4[sum_up] + part1[sum_up])
    for sum_down in range(row // 2):
        tmp.append(part3[sum_down] + part2[sum_down])
    return tmp


def partspinleft(arr):  #6
    tmp = []
    part1 = []
    part2 = []
    part3 = []
    part4 = []
    row = len(arr)
    col = len(arr[0])
    for r in range(row // 2):
        part1.append(arr[r][:col // 2])
        part2.append(arr[r][col // 2:])
        part4.append(arr[r + row // 2][:col // 2])
        part3.append(arr[r + row // 2][col // 2:])

    for sum_up in range(row // 2):
        tmp.append(part2[sum_up] + part3[sum_up])
    for sum_down in range(row // 2):
        tmp.append(part1[sum_down] + part4[sum_down])
    return tmp

for co in command:
    if co == 1:
        lst = updown(lst)
    elif co == 2:
        lst = leftright(lst)
    elif co == 3:
        lst = spinright(lst)
    elif co == 4:
        lst = spinleft(lst)
    elif co == 5:
        lst = partspinright(lst)
    elif co == 6:
        lst = partspinleft(lst)

for r in range(len(lst)):
    print(*lst[r])