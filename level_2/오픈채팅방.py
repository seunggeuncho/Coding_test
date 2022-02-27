def solution(record):
    
    for i in range(len(record)):
        if record[i].split(' ')[0] == "Change":
            for j in range(i):
                if record[j].split(' ')[1] == record[i].split()[1]:
                    record[j].replace(record[j].split(' ')[2],record[i].split()[2])
                    print(record[j].split()[2])
    print(record)
    answer=[]
    
    return answer
