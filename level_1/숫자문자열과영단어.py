def solution(s):
    num_dict = {'zero': 0, 'one':1,'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5 ,'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9}
    s = list(s)
    alpha=[]
    answer =[]
    wer="one"
    for i in range(len(s)):
        if s[i].isdigit():
            answer.append(s[i])
            continue
        else:
            alpha.append(s[i])
            if(''.join(alpha) in num_dict):
                str_alpha = ''.join(alpha)
                answer.append(num_dict[str_alpha])
                alpha.clear()
    answer = ''.join(list(map(str, answer)))    
    return int(answer)
