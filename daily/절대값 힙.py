import sys


sys.stdin = open('test.txt')

n = int(input())
que = []

def check(que):
    if len(que) == 0:
        print(0)
    else:
        que.sort(key= lambda x : (x[0],x[1]))
        abs_t, t = que.pop(0)
        print(t)

for _ in range(n):
    tmp = int(input())
    if tmp == 0:
        check(que)
    else:
        que.append([abs(tmp),tmp])
