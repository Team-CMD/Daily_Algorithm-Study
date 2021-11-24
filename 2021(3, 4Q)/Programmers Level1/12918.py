# 문자열 다루기 기본

def solution(s):
    answer = True

    for i in s:
        if (97 <= ord(i) <= 122) or (65 <= ord(i) <= 90) or (len(s) != 4 and len(s) != 6):
            return False
    return answer
