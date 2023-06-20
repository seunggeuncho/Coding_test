import sys; rl = sys.stdin.readline

sys.stdin = open("test.txt",'r')
cnt = 0
lst = []
while 1:
    INP = rl().rstrip()
    if INP == '-1 -1':
        break
    elif INP == '':
        continue
    
