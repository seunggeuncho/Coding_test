def solution(new_id):
    id = []
    new_id = new_id.lower()
    id = list(new_id)
    answer=''
    i = 0
    while i <len(id):
        if id[i].islower() or id[i]=='-' or id[i]=='_' or id[i]=='.' or id[i].isdigit():
            i+=1
        else:
            del id[i]
    if len(id) == 0:
        return "aaa"
    i = 0
    flag = 0
    while i<len(id):
        if id[i] == '.':
            if flag == 1:
                del id[i]
                i-=1
            flag = 1
            i+=1
        else:
            flag = 0
            i+=1
    if len(id) == 0:
        return "aaa"
    if id[0] == '.':
        del id[0]
    if len(id) == 0:
        return "aaa"
    if id[len(id)-1] == '.':
        del id[len(id) - 1]
    if len(id) == 0:
        return "aaa"
    cnt = 15
    if len(id) >= 16:
        id = id[:15]
        if id[14] == '.':
            del id[14]
    if len(id) <= 2:
        i = len(id)-1
        while len(id) !=3:
            id.append(id[i])
    answer="".join(id)
    return answer
