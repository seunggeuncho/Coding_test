def cmp(wd1, wd2):
    total = 0
    for idx in range(len(wd1)):
        if wd1[idx] != wd2[idx]:
            total += 1
    return total
def solution(begin, target, words):
    answer = []
    if words[-1] != target:
        return 0
    visit = [0 for i in range(len(words))]
    word_li = [begin]
    def DFS(word_li):
        print(word_li)
        if word_li[-1] == target:
            nonlocal answer
            answer.append(len(word_li) - 1)
            return
        for idx  in range(0, len(words)):
            print(idx)
            if visit[idx] == 0:
                if cmp(words[idx],word_li[-1]) <= 1:
                    word_li.append(words[idx])
                    visit[idx] = 1
                    DFS(word_li)
                    word_li.pop(-1)
                    visit[idx] = 0
    DFS(word_li)
    return min(answer)
