import sys
from collections import defaultdict

sys.stdin = open("test",'r')

T = int(input())

for _ in range(T):
    s_dict = defaultdict(list)
    str = input()
    W = int(input())
    min_val = float('inf')
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
            min_lst.append([val[i],val[i + W - 1]])

    if check ==0 :
        print(-1)
        continue
    max_val = 0
    for key, val in s_dict.items():
        if len(val) < 2:
            continue
        for idx in range(len(val) - 1):
            for it in min_lst:
                start, end = it
                if val[idx] <= start and val[idx + 1] >= end:
                    max_val = max(max_val, val[idx + 1] - val[idx] + 1)
    print(min_val,max_val)