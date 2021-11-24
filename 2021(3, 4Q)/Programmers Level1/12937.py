# 짝수와 홀수

def solution(num):
    answer = ''
    if num % 2 == 0:
        answer = "Even"
    elif num % 2 == 1:
        answer = "Odd"
    else:
        answer = "Even"
    return answer
