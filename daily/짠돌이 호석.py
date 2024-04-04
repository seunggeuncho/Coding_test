import sys

sys.stdin = open('test.txt','r')

n1,m1 = map(int, input().split())
lst = []
lst1 = [[0 for _ in range(150)] for _ in range(150)]
for _ in range(n1):
    lst.append(list(map(int, input())))
print(lst)

for row in range(n1):
    for col in range(m1):
        lst1[50 + row][50 + col] = lst[row][col]

n2,m2 = map(int, input().split())
lst2 = []
for _ in range(n2):
    lst2.append(list(map(int, input())))

def turn(lst):
    row = len(lst)
    col = len(lst[0])
    tmp = [[0 for _ in range(row)] for _ in range(col)]
    for r in range(row):
        for c in range(col):
            tmp[c][row - 1 - r] = lst[r][c]
    return tmp

def compare(t_lst,r,c):
    for i in range(len(t_lst)):
        for j in range(len(t_lst[0])):
            if t_lst[i][j] == 1 and lst1[i + r][j + c] == 1:
                return 0
    return 1

def check(c_lst):
    minarea = float('inf')
    tmp_r = len(c_lst)
    tmp_c = len(c_lst[0])
    for c_r in range(150 - tmp_r):
        for c_c in range(150 - tmp_c):
            if compare(c_lst,c_r,c_c) == 0:
                continue
            else:
                minx = min(c_c,50)
                miny = min(c_r ,50)
                maxx = max(c_c + tmp_c, 50 + m1)
                maxy = max(c_r + tmp_r, 50 + n1)
                minarea = min(minarea, (maxy - miny) * (maxx - minx))


    return minarea

ans = float('inf')

ans = min(ans, check(lst2))
lst2 = turn(lst2)
ans = min(ans, check(lst2))
lst2 = turn(lst2)
ans = min(ans, check(lst2))
lst2 = turn(lst2)
ans = min(ans, check(lst2))
lst2 = turn(lst2)
print(ans)