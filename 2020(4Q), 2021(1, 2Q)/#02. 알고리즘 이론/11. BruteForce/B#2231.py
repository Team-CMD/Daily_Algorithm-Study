if __name__=="__main__":
    # N값 입력
    N = int(input())
    # 결과 비교변수 res선언
    res = 0
    # 1부터 N까지 반복
    for i in range(1, N+1):
        # 숫자의 각 자릿수를 가지는 값 create와 숫자(i)를 더하여 생성자(=res)를 만들어냄
        create = list(map(int, str(i)))
        #print(create)
        res = i + sum(create)
        # 생성자가 N과 같으면 출력후 반복멈춤
        if res == N:
            print(i)
            break
        # 반복과정에서 숫자와 N이 같으면 생성자 X, 0출력
        if i == N:
            print(0)