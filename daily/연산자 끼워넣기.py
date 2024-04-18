import sys

sys.stdin =open('test.txt','r')

n = int(input())
lst = list(map(int, input().split()))
oper = list(map(int, input().split()))