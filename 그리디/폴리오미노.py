import sys

sys.stdin = open("test.txt",'r')
board = input()
seq = 0
ans = []
check = 0
for i in range(len(board)):
    if board[i] == 'X':
        seq += 1
    else:
        if seq > 0:
            while 1:
                if seq >= 4:
                    seq -= 4
                    ans.append('AAAA')
                else:
                    seq -= 2
                    ans.append('BB')
                if seq <= 0:
                    break
        if seq < 0:
            check = -1
            print(-1)
            break
        ans.append('.')
        seq = 0

if seq > 0 and check == 0:
    while 1:
        if seq >= 4:
            seq -= 4
            ans.append('AAAA')
        else:
            seq -= 2
            ans.append('BB')
        if seq <= 0:
            break
    if seq < 0:
        check = -1
        print(-1)
if check == 0:
    ans = ''.join(s for s in ans)
    print(ans)