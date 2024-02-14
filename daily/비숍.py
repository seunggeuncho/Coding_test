import sys

sys.stdin = open('test.txt','r')

size = int(input())

chess = [list(map(int, input().split())) for _ in range(size)]

