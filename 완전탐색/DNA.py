import sys

sys.stdin = open("test.txt",'r')
n, m = map(int, input().split())
lst = []
dna = ['A','C','G','T']
for _ in range(n):
    lst.append(list(input()))

total = 0
ans = []
for idx in range(m):
    hamming = float('inf')
    str = ''
    for d in dna:
        diff = 0
        for idx2 in range(n):
            if lst[idx2][idx] != d:
                diff += 1
        if hamming > diff:
            str = d
            hamming = diff
    total += hamming
    ans.append(str)
print(''.join(ans))
print(total)