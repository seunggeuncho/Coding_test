def solution(genres, plays):
    total = {}
    answer = []
    for idx in range(len(genres)):
        if genres[idx] in total.keys():
            total[genres[idx]] += plays[idx]
        else:
            total[genres[idx]] = plays[idx]
    while total: 
        play_li = []
        max_album = max(total, key = total.get)
        for idx in range(len(genres)):
            if max_album == genres[idx]:
                play_li.append(plays[idx])
        play_li.sort(reverse = True)
        if len(play_li) > 2:
            play_li = play_li[:2]
        while play_li:
            find = play_li.pop(0)
            for idx in range(len(genres)):
                if genres[idx] == max_album and plays[idx] == find and idx not in answer:
                    answer.append(idx)
                    break
        del total[max_album]
    
    return answer
