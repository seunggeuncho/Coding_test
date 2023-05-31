import sys

sys.stdin = open('../sample2.txt', 'r')
S = int(input())
total = 0
count = 0
for i in range(1, S + 1):
    total += i
    if total > S:
        break
    count += 1
print(count)