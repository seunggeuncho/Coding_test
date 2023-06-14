import sys

sys.stdin = open('test','r')

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
result = []
global one
one = 0
global zero
zero = 0
def divide(x,y,N):
    anchore = lst[x][y]
    for r in range(x, x+N):
        for c in range(y, y+N):
            if anchore != lst[r][c]:
                divide(x, y, N//2)
                divide(x, y + N//2, N//2)
                divide(x + N//2, y, N//2)
                divide(x + N//2, y + N//2, N//2)
                return
    if anchore == 0:
        global zero
        zero += 1
    else:
        global one
        one += 1
divide(0,0,N)
print(zero)
print(one)

"""
zero = 0
one = 0
lst_len = len(lst)
for r in range(lst_len):
    for c in range(lst_len):
        if lst[r][c] != -1:
            cnt = 1
            anchor = lst[r][c]
            check = 1
            while 1:
                if cnt + r > N or cnt + c > N:
                    break
                for i in range(cnt):
                    for val in lst[r + i][c:c+cnt]:
                        if val != anchor:
                            check = 0
                            break
                if check == 0:
                    break
                cnt += 1
            for row in range(cnt - 1):
                for col in range(cnt - 1):
                    lst[r + row][c + col] = -1
            if anchor == 0:
                zero += 1
            elif anchor == 1:
                one += 1

print(zero)
print(one)
"""
