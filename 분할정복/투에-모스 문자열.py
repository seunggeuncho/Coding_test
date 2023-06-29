import sys

sys.stdin = open("test.txt",'r')
k = int(input())
"""
str = '0'
def mose(str):
    if len(str) >= k:
        return str
    tmp = ''
    for i in str:
        if i == '1':
            tmp += '0'
        else:
            tmp += '1'

    return mose(str + tmp)

print(mose(str)[k - 1])
"""
def mose(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif x % 2 == 0:
        return mose(x // 2)
    else:
        return 1 - mose(x // 2)
print(mose(k - 1))