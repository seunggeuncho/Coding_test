import sys
from collections import deque

sys.stdin = open('../sample2.txt', 'r')
N,M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
info = [list(map(int, input().split())) for _ in range(M)]   #명령 정보

dir = [[0,0],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]
rain_map = [[N-1,0],[N-1,1],[N-2,0],[N-2,1]]    #배열은 0부터 시작해서 -1씩
ans = 0
#------------------초기화
def check(x,y): #대각선 체크 함수
    total = 0
    for idx in range(2,9,2):
        dx = x + dir[idx][0]
        dy = y + dir[idx][1]
        if 0 <= dx <= N - 1 and 0 <= dy <= N - 1:
            if maps[dx][dy] >= 1:
                total += 1
    return total

for i in info:
    visited =[[0 for _ in range(N)] for _ in range(N)]
    rain_map = deque(rain_map)
    direction, dis = i
    move_cloud = []    #움직인 구름
    while rain_map:
        x, y = rain_map.popleft()
        x += dir[direction][0] * dis
        y += dir[direction][1] * dis
        move_cloud.append([x % N,y % N])
        visited[x%N][y%N] = 1
    for cloud in move_cloud:
        maps[cloud[0]][cloud[1]] += 1   #여기서 오류 아래 check함수 코드를 이 for문에서 같이 돌리면 값이 다르게 나옴
    for cloud in move_cloud:
        maps[cloud[0]][cloud[1]] += check(cloud[0],cloud[1])
    for r in range(N):
        for c in range(N):
            if visited[r][c] == 0 and maps[r][c] >= 2:
                rain_map.append([r,c])
                maps[r][c] -= 2
for r in range(N):
    for c in range(N):
        ans += maps[r][c]
print(ans)