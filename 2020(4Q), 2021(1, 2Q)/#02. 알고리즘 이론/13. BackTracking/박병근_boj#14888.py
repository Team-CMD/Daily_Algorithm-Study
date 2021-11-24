# 연산자 끼워넣기
'''
입력
첫째줄 = N(2~11)
둘째줄 = 수열
셋째줄 = 연산자

출력
첫째줄 = 식의 결과들 중 최댓값
둘째줄 = 식의 결과들 중 최솟값
'''

# num = [숫자를 입력하는 리스트]
# num_hap = [무작위 연산자 배치를 통해 얻은 값을 저장한 리스트]


# 백준이 원하는 결과는 주지만 시간초과 됨 ㅠ.ㅠ

import sys          #시간초과 때문에 input대신 sys.stdin.readline을 사용하기위해 선언
def col(cnt, hap, plus, mi, mul, div):  # 연산자와 숫자들을 이용해 계산을 해주는 재귀함수
    global num_hap
    global max_hap, min_hap
    global N                
    if cnt == N:               # 카운트와 입력한 숫자의 개수가 같으면 조건실행 
        num_hap.append(hap)     # 숫자와 연산자들로 구한 값을 num_hap 리스트의 저장
        max_hap = max(num_hap)  # 재귀 될 때마다 리스트의 저장된 값 중 최댓값을 max_hap의 새로 저장
        min_hap = min(num_hap)  # 재귀 될 때마다 리스트의 저장된 값 중 최솟값을 min_hap의 새로 저장
        return
    
    if plus :      # 더하기가 골라졌을 때
        col(cnt+1, hap + num[cnt], plus-1, mi, mul, div)
    if mi :         # 빼기가 골라졌을 때
        col(cnt+1, hap - num[cnt], plus, mi-1, mul, div)
    if mul :        # 곱하기가 골라졌을 때
        col(cnt+1, hap * num[cnt], plus, mi, mul-1, div)
    if div :        # 나누기가 골라졌을 때
        if hap < 0:
            hap = -(-hap // num[cnt])
        else :
            hap = hap // num[cnt]
        col(cnt+1, hap, plus, mi, mul, div-1) 
# 각 케이스 별로 백트래킹을 사용해 연산자와 숫자의 모든 조합을 한번씩 다 구해 num_hap의 값을 저장함
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    num = list(map(int, sys.stdin.readline().split()))
    oper = list(map(int, sys.stdin.readline().split()))
    num_hap = []
    max_hap = 0
    min_hap = 0
    col(1, num[0], oper[0], oper[1], oper[2], oper[3])  # cnt는 연산자의 수가 숫자의 개수보다 1개 작으므로 1부터 시작
    print(max_hap)                                      # 2번째는 첫번째 숫자의 값을 3번째부터 6번째까지는 각 연산자의 갯수를 넣어줌
    print(min_hap)
    

    

