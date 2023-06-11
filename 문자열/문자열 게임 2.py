import sys
from collections import defaultdict

sys.stdin = open("test",'r')

T = int(input())

for _ in range(T):
    s_dict = defaultdict(list)
    str = input()
    W = int(input())
    min_val = float('inf')
    max_val = 0
    for idx in range(len(str)):
        s_dict[str[idx]].append(idx)
    check = 0
    min_lst = []
    for key, val in s_dict.items():
        if len(val) < W:
            continue
        check = 1
        for i in range(len(val) - W + 1):
            min_val = min(val[i + W - 1] - val[i] + 1,min_val)
            max_val = max(max_val, val[i + W - 1] - val[i] + 1)
    if check ==0 :
        print(-1)
        continue
    print(min_val,max_val)