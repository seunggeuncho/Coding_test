import sys

sys.stdin = open('../sample.txt', 'r')
N = int(input())
student = []    #자리에 앉는 학생 순서
favor = []      #각 학생이 좋아하는 학생의 번호
dir =[[0,1],[0,-1],[1,0],[-1,0]]    #인접칸 확인을 위한 방향
class_room = [[0 for _ in range(N)] for _ in range(N)]  #교실
for i in range(N ** 2):
    tmp = list(map(int,input().split()))
    student.append(tmp[0])
    favor.append(tmp[1:])

for idx in range(len(student)):
    total = []
    for row in range(N):
        for col in range(N):
            if class_room[row][col] != 0:
                continue
            fav_count = 0
            empty_count = 0
            for i in range(4):
                t_row = row + dir[i][0]
                t_col = col + dir[i][1]
                if 0 <= t_row < N and 0 <= t_col < N:
                    if class_room[t_row][t_col] in favor[idx]:
                        fav_count += 1
                    if class_room[t_row][t_col] == 0:
                        empty_count += 1
            total.append([fav_count, empty_count, row, col])
    total.sort(key = lambda x : (-x[0],-x[1],x[2],x[3]))
    class_room[total[0][2]][total[0][3]] = student[idx]

result = 0
for r in range(N):
    for c in range(N):
        cur = class_room[r][c]
        cur_val = 0
        for i in range(4):
            t_row = r + dir[i][0]
            t_col = c + dir[i][1]
            if 0 <= t_row < N and 0 <= t_col < N:
                if class_room[t_row][t_col] in favor[student.index(cur)]:
                    cur_val += 1
        if cur_val == 1:
            result += 1
        elif cur_val == 2:
            result += 10
        elif cur_val == 3:
            result += 100
        elif cur_val == 4:
            result += 1000
print(result)


