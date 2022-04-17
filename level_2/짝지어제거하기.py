def solution(s):
    
    s = list(s)
    idx2 = 0
    while(idx2 < len(s)):
        idx = 0
        while (idx < len(s) - 1):
            if s[idx] == s[idx + 1]:
                s.pop(idx)
                s.pop(idx)
                idx += 1
                break
            idx += 1
        if len(s) <= 1:
            break
        idx2 +=1
    print(s)
    if len(s) >= 1:
        return 0
    return 1
solution(s)
