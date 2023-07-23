import sys

sys.stdin = open('test.txt','r')
n = int(input())
rope = []
for _ in range(n):
    rope.append(int(input()))
ans = 0
rope.sort(reverse=True)
for i in range(len(rope)):
    ans = max(ans, rope[i] * (i + 1))
print(ans)


