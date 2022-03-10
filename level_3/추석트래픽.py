"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]
def tim_diff(time,dur):
    hour,minute, sec = time.split(':')[0], time.split(':')[1], time.split(':')[2]
    new_sec = sec-dur
    if (new_sec < 0):
        new_sec = 60 + sec - dur
        new_minute = minute - 1
        if (new_minute < 0):
            new_minute = 60 + minute - 1
            new_hour = new_hour - 1
        
        
def solution(lines):
    answer = 0
    time_list = []
    for line in lines:
        times = line.split()
        time, dur = times[1], times[2]
        dur = float(dur[:-1])
        
        
    return answer
solution(lines)

