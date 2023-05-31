import sys

sys.stdin = open('sample.txt', 'r')
N,M = map(int, input().split())
lst = []    #격자
cmd = []
for i in range(N):
    lst.append(list(map(int, input().split())))

for j in range(M):
    cmd.append(list(map(int, input().split())))

dir = [[1,0],[0,1],[-1,0],[0,-1]]   #회전을 위한 방향
shark = [int((N + 1) / 2 - 1),int((N + 1) / 2 - 1)]

remove_dir = [[0,0],[-1,0],[1,0],[0,-1],[0,1]]  #삭제를 위한 방향
answer = 0
#초기화 끝
for command in cmd:
    direc, dis = command
    row, col = shark[0],shark[1]
    for d in range(dis):    #주어진 방향으로 거리만큼 삭제
        row = row + remove_dir[direc][0]
        col = col + remove_dir[direc][1]
        lst[row][col] = 0

    pos = [int((N + 1) / 2 - 1), int((N + 1) / 2 - 2)]  # 처음 위치
    tmp = []
    if lst[pos[0]][pos[1]] != 0:
        tmp.append(lst[pos[0]][pos[1]])
    for cur in range(3, N + 2,2):   #회전하면서 값 받아오기
        for d in range(cur - 2):
            pos[0] = pos[0] + dir[0][0]
            pos[1] = pos[1] + dir[0][1]
            if lst[pos[0]][pos[1]] != 0:
                tmp.append(lst[pos[0]][pos[1]])
        for r in range(cur - 1):
           # print(pos[0], pos[1])
            # print(lst[pos[0]][pos[1]])
            pos[0] = pos[0] + dir[1][0]
            pos[1] = pos[1] + dir[1][1]
            if lst[pos[0]][pos[1]] != 0:
                tmp.append(lst[pos[0]][pos[1]])
        for u in range(cur - 1):
            #print(pos[0], pos[1])
            #   print(lst[pos[0]][pos[1]])
            pos[0] = pos[0] + dir[2][0]
            pos[1] = pos[1] + dir[2][1]
            if lst[pos[0]][pos[1]] != 0:
                tmp.append(lst[pos[0]][pos[1]])
        if cur == N:
            for l in range(cur -1):
                pos[0] = pos[0] + dir[3][0]
                pos[1] = pos[1] + dir[3][1]
                if lst[pos[0]][pos[1]] != 0:
                    tmp.append(lst[pos[0]][pos[1]])
             #   print(pos[0], pos[1])
        else:
            for l in range(cur):
              #  print(pos[0], pos[1])
                #     print(lst[pos[0]][pos[1]])
                pos[0] = pos[0] + dir[3][0]
                pos[1] = pos[1] + dir[3][1]
                if lst[pos[0]][pos[1]] != 0:
                    tmp.append(lst[pos[0]][pos[1]])

    while 1:    #4개 이상 연속된 구술 삭제하기
        check = 0
        idx = 0
        while idx < len(tmp):

            t_idx = idx + 1
            cnt = 0
            while t_idx < len(tmp):
                if tmp[idx] == tmp[t_idx]:
                    cnt += 1
                else:
                    break
                t_idx += 1

            if cnt >= 3:
                check = 1
                if tmp[idx] == 1:
                    answer += (cnt + 1)
                elif tmp[idx] == 2:
                    answer += (cnt + 1) * 2
                elif tmp[idx] == 3:
                    answer += (cnt + 1) * 3
                tmp = tmp[:idx] + tmp[idx + cnt + 1:]
                break
            idx += 1
        if check == 0:
            break

    idx = 0
    final = []
    while idx < len(tmp):       #구슬 변환
        t_idx = idx + 1
        if t_idx < len(tmp):
            if tmp[idx] != tmp[t_idx]:
                final.append(1)
                final.append(tmp[idx])
                idx += 1
                continue
        cnt = 1
        while t_idx < len(tmp):
            if tmp[idx] == tmp[t_idx]:
                cnt += 1
            else:
                break
            t_idx += 1
        final.append(cnt)
        final.append(tmp[idx])
        idx += cnt

    pos = [int((N + 1) / 2 - 1), int((N + 1) / 2 - 2)]  # 처음 위치
    if len(final) >= 1:
        lst[pos[0]][pos[1]] = final[0]
    else:
        lst[pos[0]][pos[1]] = 0

    idx = 1
    for cur in range(3, N + 2,2):
        for d in range(cur - 2):
            pos[0] = pos[0] + dir[0][0]
            pos[1] = pos[1] + dir[0][1]
            if idx < len(final):
                lst[pos[0]][pos[1]] = final[idx]
            else:
                lst[pos[0]][pos[1]] = 0
            idx += 1

        for r in range(cur - 1):
            pos[0] = pos[0] + dir[1][0]
            pos[1] = pos[1] + dir[1][1]
            if idx < len(final):
                lst[pos[0]][pos[1]] = final[idx]
            else:
                lst[pos[0]][pos[1]] = 0
            idx += 1
        for u in range(cur - 1):

            pos[0] = pos[0] + dir[2][0]
            pos[1] = pos[1] + dir[2][1]
            if idx < len(final):
                lst[pos[0]][pos[1]] = final[idx]
            else:
                lst[pos[0]][pos[1]] = 0
            idx += 1

        if cur == N:    #마지막 테두리
            for l in range(cur -1):
                pos[0] = pos[0] + dir[3][0]
                pos[1] = pos[1] + dir[3][1]
                if idx < len(final):
                    lst[pos[0]][pos[1]] = final[idx]
                else:
                    lst[pos[0]][pos[1]] = 0
                idx += 1
        else:
            for l in range(cur):
                pos[0] = pos[0] + dir[3][0]
                pos[1] = pos[1] + dir[3][1]
                if idx < len(final):
                    lst[pos[0]][pos[1]] = final[idx]
                else:
                    lst[pos[0]][pos[1]] = 0
                idx += 1
    print(lst)
print(answer)