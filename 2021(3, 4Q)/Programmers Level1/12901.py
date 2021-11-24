# 2016년

def solution(a, b):
    answer = ''
    m = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    total = 0
    for i in range(1, a):
        total += m[i-1]
    answer = (total+b+4) % 7
    return day[answer]
