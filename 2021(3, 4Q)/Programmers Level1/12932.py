# 자연수 뒤집어 배열로 만들기

def solution(n):
    answer = []
    answer = list(str(n))
    answer.reverse()
    for i in range(len(answer)):
        answer[i] = int(answer[i])

    return answer
