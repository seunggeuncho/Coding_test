import sys
import copy

sys.stdin = open("test",'r')
N = int(input())
egg_info = []
for _ in range(N):
    egg_info.append(list(map(int, input().split())))

egg_length = len(egg_info)
global ans
ans = 0

def count_egg(egg_info):
    result = 0
    for i in range(len(egg_info)):
        if egg_info[i][0] <= 0:
            result += 1
    return result

def dfs(idx,egg_info):
    if idx == egg_length:
        tmp = count_egg(egg_info)
        global ans
        ans = max(ans, tmp)
        return
    if egg_info[idx][0] <= 0:
        dfs(idx + 1, egg_info)
        return

    check = 1
    for i in range(egg_length):
        if i == idx:
            continue
        if egg_info[i][0] > 0:
            check = 0
    if check == 1:
        tmp = count_egg(egg_info)
        ans = max(ans, tmp)
        return
    for i in range(egg_length):
        if egg_info[i][0] > 0 and idx != i:
            egg_info[i][0] -= egg_info[idx][1]
            egg_info[idx][0] -= egg_info[i][1]
            dfs(idx + 1, egg_info)
            egg_info[i][0] += egg_info[idx][1]
            egg_info[idx][0] += egg_info[i][1]
dfs(0, egg_info)
print(ans)


"""
ans = 0
for idx in range(len(egg_info)):
    dur, weight = egg_info[idx]
    if dur <= 0:
        continue
    for _idx in range(idx, len(egg_info)):
        cmp_dur, cmp_weight = egg_info[_idx]
        if cmp_dur <= 0: #이미 깨진 다른 계란
            continue
        cmp_dur -= weight   #계란 치기
        dur -= cmp_dur
        egg_info[idx][0] = dur
        egg_info[_idx][0] = cmp_dur
        if dur <= 0: #손에 들고있던 계란이 깨지면 끝
            ans += 1
            break
        if cmp_dur <= 0: #비교한 계란이 깨지면 +1
            ans += 1
print(ans)"""
