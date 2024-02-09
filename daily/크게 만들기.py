import sys

sys.stdin = open('test.txt','r')

n,k = map(int, input().split())
final = n - k
num = list(input())
answer = []

while len(answer) < final:
    strd = num[0]
    indx = 0
    for idx in range(1,1 + k):
        if strd < num[idx]:
            strd = num[idx]
            indx = idx
    answer.append(strd)
    num = num[indx + 1:]
    k -= indx
print(int(''.join(answer)))