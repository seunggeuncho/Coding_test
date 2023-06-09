import sys

sys.stdin = open('test','r')
T = int(input())

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

