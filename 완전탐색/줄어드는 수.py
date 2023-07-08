import sys

sys.stdin = open('test.txt','r')
n = int(input())
global lst
lst= [i for i in range(10)]
"""
def check(t,cnt):
    if cnt == len(t) - 1:
        lst.append(int(''.join(t)))
        return
    if t[cnt] > t[cnt + 1]:
        check(t, cnt + 1)
    else:
        return
flag = 0
for t in range(11, 987654322):
    if len(lst) >= n:
        print(lst[n - 1])
        print(lst)
        flag = 1
        break
    check(list(str(t)),0)

if flag == 0:
    print(-1)
"""
def make(tmp, cnt):
    if len(tmp) == cnt:
        global lst
        if cnt > 1:
            lst.append(int(''.join(tmp)))
        return
    for i in range(0,10):
        if not tmp:
            tmp.append(str(i))
            make(tmp,cnt)
            tmp.pop(-1)
        else:
            if int(tmp[-1]) > i:
                tmp.append(str(i))
                make(tmp,cnt)
                tmp.pop(-1)
flag = 1
for i in range(2,11):
    make([],i)
    if len(lst) >= n:
        lst.sort()
        print(lst[n - 1])
        flag = 0
        break
if flag == 1:
    lst.sort()
    print(-1)