# 약수의 개수와 덧셈

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        n = 0
        for j in range(1, int(i**(1/2))+1):
            if (i % j == 0):
                n += 1
                if ((j**2) != i):
                    n += 1
        if (n % 2 == 0):
            answer += i
        else:
            answer -= i
    return answer
