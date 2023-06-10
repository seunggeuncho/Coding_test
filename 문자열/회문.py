import sys

sys.stdin = open('test','r')
T = int(input())
"""
for _ in range(T):
    str = list(input())
    if str == str[::-1]:
        print(0)
        continue
    check = 0
    for idx in range(len(str)):
        tmp = str[:idx] + str[idx + 1:]
        if tmp == tmp[::-1]:
            print(1)
            check = 1
            break
    if check == 0:
        print(2)

"""
for _ in range(T):
    str = list(input())
    last = len(str) - 1
    start = 0
    check = 1
    while start <= last:
        if str[start] == str[last]:
            start += 1
            last -= 1
            continue
        if str[start] != str[last]:
            tmp = str[:start] + str[start + 1:]
            if tmp == tmp[::-1]:
                check = 0
                print(1)
                break
            tmp = str[:last] + str[last + 1:]
            if tmp == tmp[::-1]:
                print(1)
                check = 0
                break
            break

    if start >= last:
        print(0)
    else:
        if check == 1:
            print(2)
