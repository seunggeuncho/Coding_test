import sys

sys.stdin = open("test.txt",'r')
n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input())))
global ans
ans = ''
def check(x,y,n):
    global ans
    stand = lst[x][y]
    for r in range(x, x + n):
        for c in range(y, y + n):
            if stand != lst[r][c]:
                ans += '('
                check(x, y, n // 2)
                check(x, y + n // 2, n //2)
                check(x + n // 2, y, n // 2)
                check(x + n // 2, y + n // 2, n // 2)
                ans += ')'
                return
    ans += str(stand)


check(0,0,n)
print(ans)