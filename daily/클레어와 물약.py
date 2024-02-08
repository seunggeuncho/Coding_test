"""
from collections import deque
import sys


sys.stdin = open('test.txt','r')
n, m = map(int, input().split())

# 물약 사용 여부
visited = [False] * (n + 1)
# nxt_recipe[i] : (i번 물약을 통해 다음으로 갈 수 있는 물약의 번호, 해당 레시피 번호) 의 리스트
nxt_recipe = [[] for _ in range(n + 1)]
# 레시피의 차수
indegree = [0] * (m + 1)
# 레시피 정보
recipe_info = []

# 위상정렬을 위한 queue
q = deque()

# 레시피 내용 반영
for j in range(m):
    inputs = list(map(int, input().split()))

    for i in range(1, len(inputs) - 1):
        # inputs[i] -> inputs[-1] : topological sort
        nxt_recipe[inputs[i]].append((inputs[-1], j))
        indegree[j] += 1

    recipe_info.append(inputs[1:])

# 현재 가지고 있는 물약의 개수
l = int(input())

# 현재 가지고 있는 물약
result = list(map(int, input().split()))

# 현재 물약을 가지고 레시피들의 차수 계산
for liquid in result:
    # 물약 사용 여부 체크
    visited[liquid] = True

    # 해당 물약으로부터 다음 물약으로 갈 수 있는 레시피 차수 감소
    for next in nxt_recipe[liquid]:
        indegree[next[1]] -= 1
        if indegree[next[1]] == 0:
            # 레시피 차수가 0이라면 진입이 가능하므로 레시피 번호에 있는 입력 레시피 삽입
            q.append(recipe_info[next[1]])
# 위상 정렬
print(nxt_recipe)
while q:
    r_info = q.popleft()

    # 만들어질 물약이 이미 사용되었을 경우 continue
    if visited[r_info[-1]]:
        continue

    # 물약 사용 체크
    visited[r_info[-1]] = True
    # 결과에 값 기록
    result.append(r_info[-1])

    # 해당 물약으로부터 다음 물약으로 갈 수 있는 레시피 차수 감소
    for next in nxt_recipe[r_info[-1]]:
        indegree[next[1]] -= 1
        if indegree[next[1]] == 0:
            # 레시피 번호에 있는 입력 레시피 삽입
            q.append(recipe_info[next[1]])

# 결과 출력
print(len(result))
print(' '.join(map(str, sorted(result))))
"""

from collections import deque
import sys

sys.stdin = open('test.txt','r')

n,m = map(int, input().split())
check = [0] * (n + 1)   #만든 물약 확인
nxt_potion = [[] for _ in range(n + 1)] #인덱스 번호의 물약이 새로운 물약을 만드는 경우, 인덱스 = 현재 물약, [a,b] a = 다음 물약, b는 레시피 번호
recipe = []
count = [0] * (m) #인덱스 포션을 만들기 위해 필요한 포션의 개수

for i in range(m):
    lst = list(map(int, input().split()[1:]))
    recipe.append(lst)
    for idx in range(len(lst) - 1):
        nxt_potion[lst[idx]].append([lst[-1], i])
        count[i] += 1

l = int(input())

already_have = list(map(int, input().split()))
answer = []

q = deque()
for val in already_have:
    check[val] = 1
    answer.append(val)
    for tmp in nxt_potion[val]:
        count[tmp[1]] -= 1
        if count[tmp[1]] == 0:
            q.append(tmp[0])

while q:
    now = q.popleft()
    if check[now] == 1:
        continue
    check[now] = 1
    answer.append(now)
    for lst in nxt_potion[now]:
        count[lst[1]] -= 1
        if count[lst[1]] == 0:
            q.append(lst[0])

print(len(answer))
answer.sort()
print(*answer)
