import sys

sys.stdin = open('test.txt','r')
n = int(input())
mine = []
result = []
for _ in range(n):
    mine.append(list(input()))
for _ in range(n):
    result.append(list(input()))

def check_mine(x,y,lst):
    