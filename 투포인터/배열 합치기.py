import sys
import heapq
sys.stdin = open("test.txt",'r')
a, b = map(int, input().split())

a_lst = list(map(int, input().split()))
b_lst = list(map(int, input().split()))
lst = []
for val in a_lst:
    heapq.heappush(lst, val)
for val in b_lst:
    heapq.heappush(lst, val)

for i in range(len(lst)):
    tmp = heapq.heappop(lst)
    print(tmp, end = ' ')