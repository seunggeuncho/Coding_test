import sys
from collections import defaultdict

sys.stdin = open('test.txt','r')

n = int(input())
lst = []
key_lst = []
dic = defaultdict()
for i in range(n):
    tmp1, tmp2 = input().split(' is ')
    dic[tmp1] = tmp2
    key_lst.append(tmp1)
m = int(input())

def check(tmp1, tmp2):
    if tmp1 not in key_lst:
        return False
    if dic[tmp1] != tmp2:
        return check(dic[tmp1],tmp2)
    return True

for i in range(m):
    tmp1, tmp2 = input().split(' is ')
    if check(tmp1,tmp2) == True:
        print("T")
    else:
        print("F")