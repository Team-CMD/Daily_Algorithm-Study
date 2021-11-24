# 음양 더하기

def solution(absolutes, signs):
    answer = 123456789

    for i in range(len(absolutes)):
        if signs[i] == 'false':
            absolutes[i] *= -1
    answer = sum(absolutes)

    return answer
