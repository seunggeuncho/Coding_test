import sys

sys.stdin = open("test",'r')

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
def divide(lst):
    hq = []
    tmp = []
    next_lst = []
    next_len = len(lst) // 2
    for r in range(0,len(lst),2):
        for c in range(0, len(lst), 2):
            for i in range(2):
                for j in range(2):
                    hq.append(lst[r+i][c + j])
            hq.sort()
            tmp.append(hq[2])
            if len(tmp) == next_len:
                next_lst.append(tmp)
                tmp = []
            hq = []
    if len(next_lst[0]) == 1:
        print(next_lst[0][0])
        return
    divide(next_lst)
divide(lst)
