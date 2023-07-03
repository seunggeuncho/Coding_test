import sys

sys.stdin = open("test.txt",'r')
n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input())))
print(lst)

def check(n, ):