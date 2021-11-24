# 이상한 문자 만들기

def solution(s):
    answer = ''
    s = list(s.split(" "))
    for i in range(len(s)):
        s[i] = list(s[i])
        for j in range(len(s[i])):
            if j % 2 == 0 and 97 <= ord(s[i][j]) <= 122:
                s[i][j] = chr(ord(s[i][j]) - 32)
            elif j % 2 == 1 and 65 <= ord(s[i][j]) <= 90:
                s[i][j] = chr(ord(s[i][j]) + 32)
                print(s[i][j])
        s[i] = ''.join(s[i])
    answer = ' '.join(s)

    return answer
