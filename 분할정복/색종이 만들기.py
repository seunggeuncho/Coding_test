import sys

sys.stdin = open('test','r')

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
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