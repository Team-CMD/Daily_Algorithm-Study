'''
양의 정수 X의 각 자리가 등차수열 -> X를 수한

입력값 ->  1<= N <= 1000
1 <= count(한수) <= N

ex) 입력값 = 110
    출력값 = 99

369 => (3-6) = (6-9)
130 => (1-3) != (3-0)
310 => (3-1) != (1-0)

input = 123 -> 한수

input = 139 -> 한수 x

input = 13

숫자의 자릿수 = 1, 2, 3
1자리 수 : 1 ~ 9 => 한수
2자리 수 : 10 ~ 99 => 한수

3자리 수 : 100 ~ 999 => 각 숫자마다 달라.

'''
def yeah(N):
    # 범위는 1 ~ N
    tmp = 0 # 주어진 범위내의 한수의 갯수 

    for i in range(1,N+1):
        if i//100 == 0:
            tmp += 1
        else:
            Third = i%100
            Second = (i//10)-(Third*10)
            First = i%10
            if (Third-Second) == (Second-First):
                tmp += 1
    print(tmp)

if __name__ == "__main__":
    # input part
    N = int(input())
    # calling the function, return value
    yeah(N)