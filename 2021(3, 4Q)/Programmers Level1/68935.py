# 3진법 뒤집기

def solution(n):
    answer = 0
    tmp = []
    while(n//3 != 0):
        tmp.append(n % 3)
        n = n//3
    tmp.append(n)
    tmp.reverse()
    for i in range(len(tmp)):
        answer = answer + (3 ** i)*tmp[i]

    return answer
