def enter(ex):
    ex = ex + "님이 들어왔습니다."
    return ex

def leave(ex):
    ex = ex + "님이 나갔습니다."
    return ex
def list(record):
    list = [0 for i in range(len(record))]
    for i in range(len(record)):
        if record[i].split(' ')[0] == "Leave":
            for j in range(i):
                if record[j].split(' ')[1] == record[i].split(' ')[1] and record[j].split(' ')[0] != "Leave" :
                    list[i] = record[j].split(' ')[2]
        elif record[i].split(' ')[0] == "Change":
            list[i] = 0
        else:
            list[i] = record[i].split(' ')[2]
    return list
    
def solution(record):
    lst = list(record)
    print(lst)
        
    for i in range(len(record)):
        if record[i].split(' ')[0] == "Change" or record[i].split(' ')[0] == "Enter":
            for j in range(i):
                if record[j].split(' ')[1] == record[i].split()[1]:
                    lst[j] = record[i].split()[2]
                    
    for i in range(len(record)):
        if record[i].split(' ')[0] == "Enter":
            lst[i] = enter(lst[i])
        elif record[i].split(' ')[0] == "Leave":
            lst[i] = leave(lst[i])
        elif lst[i] == 0:
            del lst[i]
    answer = lst
    return answer
