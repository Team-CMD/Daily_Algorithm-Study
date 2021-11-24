# 문자열 니림차순으로 배치하기

def solution(s):
    answer = ''
    s = list(s)
    for i in range(len(s)):
        s[i] = ord(s[i])
    s.sort()
    s.reverse()
    for i in range(len(s)):
        s[i] = chr(s[i])
    answer = ''.join(s)
    return answer
