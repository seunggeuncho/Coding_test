import sys

sys.stdin = open("test.txt",'r')
lst = []    #빙고판
command = [] #사회자가 부르는 수
check_bingo = [] #빙고 체크

for _ in range(5):
    lst.append(list(map(int,input().split())))

for _ in range(5):
    command.append(list(map(int,input().split())))

def change(val):    #불린 숫자는 -1로 변경
    for r in range(5):
        for c in range(5):
            if lst[r][c] == val:
                lst[r][c] = -1
                break

def checks():
    cnt = 0
    for i in range(5):  #row check
        check = 0
        for j in range(5):
            if -1 != lst[i][j]:
                check = 1
                break
        if check == 0:
            cnt += 1

    for i in range(5):  #col check
        check2 = 0
        for j in range(5):
            if lst[j][i] != -1:
                check2 = 1
                break
        if check2 == 0:

            cnt += 1

    cross_check =0
    for i in range(5):  #오른쪽 대각선 체크
        if lst[i][i] != -1:
            cross_check = 1
            break
    if cross_check == 0:
        cnt += 1

    cross_check = 0
    for i in range(5):  #왼쪽 대각선 체크
        check = 0
        if  lst[i][4 - i] != -1:
            cross_check = 1
            break
    if cross_check == 0:
        cnt += 1


    if cnt >= 3:
        return 1
    else:
        return 0

for r in range(5):
    check = 0
    for c in range(5):
        if r * 5 + c >= 12:
            if checks() == 1:
                print(r * 5 + c)
                check = 1
                break
        change(command[r][c])
    if check == 1:
        break