def solution(lines):
    answer = 0
    for line in lines:
        times = line.split()
        time, sec = times[1], times[2]
        hour = time.split(':')[0]
        min = time.split(':')[1]
        second = time.split(':')[2]
        print(hour, min, second)
    
    return answer
