import re


def solution(s):
    lst = []
    for i in range(1, len(s)//2 + 1):
        reList = re.sub('(\w{%i})' %i, '\g<1> ', s).split()
        lst.append(reList)
    count=1
    flag = 0
    for num in range(len(lst)):
        re_lst= []
        update_list = lst[num]
        for i in range (len(update_list)):
            if i < len(update_list) - 1 and update_list[i] == update_list[i+1]:
                count += 1
            else:
                if count == 1:
                    re_lst.append(update_list[i])
                elif count >= 2:
                    re_lst.append(str(count)+update_list[i])
                    count = 1
        lst_len = len(''.join(re_lst))
        if flag == 0:
            answer = lst_len
            flag = 1
        if flag == 1 and answer > lst_len:
            answer = lst_len
    return answer
/////////////////////
런타임 에러(1)
