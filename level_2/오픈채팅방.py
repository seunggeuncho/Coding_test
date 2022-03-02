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
                    break
        elif record[i].split(' ')[0] == "Change":
            list[i] = 0
        else:
            list[i] = record[i].split(' ')[2]
    return list
    
def solution(record):
    lst = list(record)
    for i in range(len(record)):
        if record[i].split(' ')[0] == "Change" or record[i].split(' ')[0] == "Enter":
            for j in range(i):
                if record[j].split(' ')[1] == record[i].split()[1] and record[j].split()[0] != "Change":
                    lst[j] = record[i].split()[2]
    flag = 0
    k = 0
    for i in range(len(record)):
        if record[i - k].split(' ')[0] == "Enter":
            lst[i] = enter(lst[i])
        elif record[i - k].split(' ')[0] == "Leave":
            lst[i] = leave(lst[i])
        elif lst[i - k] == 0 and flag == 1:
            lst_num = i - k
            del lst[lst_num]
            k += 1
        elif lst[i - k] == 0:
            del lst[i]
            k += 1
            flag = 1
    answer = lst
    return answer

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

(딕셔너리를 써서 userid에 대한 user_profile_name을 설정하고 또한 튜플을 사용하여 조금 더 가독성 좋게 바꾸었다. 또한 튜플을 배열에 넣고 넣은 튜플을 배열과 같이 쓸 수 있는 점을 알 수 있었음.)

def solution(record):
    userdata = dict()
    answer = []
    user_lst = []
    
    for event in range(len(record)):
        us_event, us_id = record[event].split()[0], record[event].split()[1]
        if us_event in ("Enter","Change"):
            us_profile = record[event].split()[2]
            userdata[us_id] = us_profile
        user_lst.append((us_event, us_id))
    for user in user_lst:
        user_event, user_id = user[0], user[1]
        if user_event == "Enter":
            answer.append(f'{userdata[user_id]}님이 들어왔습니다.')
        elif user_event == "Leave":
            answer.append(f'{userdata[user_id]}님이 나갔습니다.')
    return answer







