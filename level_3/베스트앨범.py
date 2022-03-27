def solution(genres, plays):
    total = {}
    for idx in range(len(genres)):
        if genres[idx] in total.keys():
            total[genres[idx]] += plays[idx]
        else:
            total[genres[idx]] = plays[idx]
    print(total)
    answer = []
    return answer
