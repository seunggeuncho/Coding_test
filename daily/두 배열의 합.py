import sys
import bisect

sys.stdin = open('test.txt','r')

t = int(input())
n = int(input())
lst1 = list(map(int, input().split()))
m = int(input())
lst2 = list(map(int, input().split()))

result = 0
sum1 = lst1
sum2 = lst2

for start in range(n):
    for end in range(start + 1, n):
        sum1.append(sum(lst1[start:end + 1]))


for start in range(m):
    for end in range(start + 1, m):
        sum2.append(sum(lst2[start:end + 1]))


sum1.sort()
sum2.sort()

for i in range(len(sum1)):
    left = bisect.bisect_left(sum2, t - sum1[i])
    right = bisect.bisect_right(sum2, t - sum1[i])
    result += right - left
print(result)