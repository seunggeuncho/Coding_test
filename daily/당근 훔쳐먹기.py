import sys

sys.stdin = open('test.txt','r')
n,t = map(int, input().split())
carrot = []
nutrition = []
for _ in range(n):
    car, nut = map(int, input().split())
    carrot.append(car)
    nutrition.append(nut)

rest = n - 1
ans = 0
for val in range(t):
    for idx in range(n):
        carrot[idx] += nutrition[idx]
    carrot.sort(reverse=True)

    if t - val == rest:
        ans += carrot[rest]
        rest -= 1
print(ans)


