def solution(s):
    answer = 100000000
    if len(s) == 1:
        return 1
    for slicing in range(1,len(s)//2 + 1):
        tmp = s[:slicing]
        cnt = 1
        res = ''
        for idx in range(slicing , len(s) + slicing, slicing):
            if tmp == s[idx:slicing + idx]:
                cnt += 1
            else:
                if cnt == 1:
                    res += tmp
                else:
                    
                    res += str(cnt) + tmp
                tmp = s[idx:slicing + idx]
                cnt = 1
        answer = min(answer,len(res))
        
    
                
    return answer
