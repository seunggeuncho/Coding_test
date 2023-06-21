import sys
from collections import defaultdict
sys.stdin = open("test.txt",'r')
cnt = 0
dic = defaultdict(int)
while 1:
    INP = str(input().rstrip())
    print(INP)
    if not INP:
        break
    dic[INP] += 1
    cnt += 1

print(cnt)
