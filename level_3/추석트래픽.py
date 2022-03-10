"2016-09-15 01:00:04.001 3.0s",
"2016-09-15 01:00:07.000 2s"
]
def rounds(num):
    return round(num,3)
def time_diff(time,dur):
    hour,minute, sec = int(time.split(':')[0]), int(time.split(':')[1]), float(time.split(':')[2])
    print(hour, minute, sec,"===========")
    print(dur)
    new_sec = sec-dur
    new_minute = minute
    new_hour = hour
    if (new_sec < 0):
        new_sec = 60 + sec - dur
        new_minute = minute - 1
        if (new_minute < 0):
            new_minute = 60 + minute - 1
            new_hour = new_hour - 1
    new_sec = new_sec + 0.001
    print(rounds(new_hour), rounds(new_minute), rounds(new_sec))
        
def solution(lines):
    answer = 0
    time_list = []
    for line in lines:
        times = line.split()
        time, dur = times[1], times[2]
        dur = float(dur[:-1])
        time_diff(time,dur)
        
    return answer
solution(lines)

