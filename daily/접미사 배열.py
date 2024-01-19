import sys

sys.stdin = open('test.txt','r')
s = input()

lst = []

for i in range(len(s)):
    lst.append(s[i:])
lst.sort()
for val in lst:
    print(val)