import sys

sys.stdin = open('../sample2.txt', 'r')
A = int(input())
T = int(input())
chant = int(input())
turn = 0
lst = []
bun = 1
degi = 1
while 1:
    turn += 1
    for _ in range(2):
       lst.append([bun,0])
       lst.append([degi,1])
       bun += 1
       degi += 1
    for _ in range(turn + 1):
        lst.append([bun,0])
        bun += 1
    for _ in range(turn + 1):
        lst.append([degi,1])
        degi += 1
    if chant == 0:
        if T <= bun:
            print(lst.index([T,0]) % A)
            break
    else:
        if T <= degi:
            print(lst.index([T,1]) % A)
            break
