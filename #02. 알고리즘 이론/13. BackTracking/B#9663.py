# <   BOJ 9663   >
# BackTracking "N - Queen"
# 체스판 -> size ( N * N )
#     N개의 퀸을 놓는다.
#     > 퀸의 이동경로 ( 가로, 세로, 대각선 )
#     퀸을 놓았을 때 서로의 퀸이 공격할 수 없다.
#         => 서로의 퀸은 이동경로가 겹치지 않는다.

# >> 서로의 퀸이 이동경로가 겹치지 않는 경우의 수

# 주어지는 값 ) N값.
# 입력 형태 ) 첫째줄에 N이 주어짐. ( 1 <= N < 15 )
# 출력 형태 ) 첫째줄에 구하고자 하는 경우의 수 출력

# -------------------------------------------------------------------

# > 의견을 많이 주고받는다.
# > 해당 문제의 풀이방법을 정해야 함.
# > 4명이서 문제를 푸는것.
#     -> 의견수합이 가장 효율적으로 이루어져야 함.

# # [Solution]
# #     1. Python 
# #         0) N을 입력받음.
# #             N = int(input())
# #         1) N*N 체스판을 만든다.
# #             1-1) list를 활용하여 체스판을 만든다.
# #             > Bord = [[0 for _ in range(N)] for  in range(N)]
# #             1-2) 초깃값 = 0, Q의 위치= 1, Q의 동선 = 2 
# #         2) 1번째 Q의 이동경로를 체크. -> 함수()
# #             2-1) i번째 Q를 (0,0)에 위치. (i=1)
# #                 2-2) i번째 Q의 동선을 체크
# #                 2-3) 체스판을 순회해서 가장 가까운 0의 위치를 탐색
# #                      (예외처리 참조)
# #                 2-4) (2-3)에서 찾은 위치에 (i+1)번째 Q를 위치시킨다.
# #         3) 2)를 N개의 Q이 놓일때까지 반복.

# #         예외처리)
# #             N*N 크기의 체스판에서 N개의 퀸이 안들어갈 경우
# =======================================================================================

# [Solution 2 : Python]

# 0. 변수 선언
#     global cnt
# 1. N을 입력받는다.
#     global N = int(input())
#     ex) N = 5
# 2. size가 N인 list를 만든다.
#     (list의 역할 : Queen의 좌표를 의미, index와 value가 각각 x, y좌표를 의미)
#     posQ = []
#     ex) posQ = []
#             pos X :   0       1       2       3       4  
#             pos Y :  ' '     ' '     ' '     ' '     ' ' 

# 3. Queen의 위치에 따른 세로줄과 대각선을 체크한다.
#     (검사는 반복, 다음 Queen으로 넘어갈 땐 재귀, cnt는 재귀함수에서)
#     ※ x가 0일때만 검출하면 모든 경우의 수가 검출됨.
#     세로줄 : 모든 value 달라야 함.
#     대각선 : index의 차이 != value의 차이

#      cnt조건 : Queen의 개수 == N

#     def nQueen(y):
#         if len(posQ) > 1:
#             for i in range(len(posQ)):
#                 if y == posQ[i]:
#                 # 가로 세로 검출
#                     return
#                 if abs(posQ[i]-y) == len(posQ)+1-i:
#                 # 대각선 검출
#                     return
#         posQ.append(y)
#         if len(posQ) == N:
#             cnt += 1
#             return

#         for i in range(N):
#             nQueen(i)
#             posQ.pop()
        
#         return
# --------------------------------------------------------------------------------
import sys
sys.setrecursionlimit(10000)

global cnt
global posQ

def nQueen(posQ:list, y:int):
    posQ.append(y)
    if len(posQ) >= 2:
        for i in range(len(posQ)-1):
            if y == posQ[i]:
                return 0

            if abs(posQ[i] - y) == (len(posQ) -1 - i):
                return 0

    if len(posQ) == N:
        return 1

    cnt = 0

    for k in range(N):
        cnt += nQueen(posQ, k)
        posQ.pop()

    return cnt


if __name__ == "__main__":
    global N
    cnt = 0
    N = int(input())

    for i in range(N):
        posQ = []
        cnt += nQueen(posQ, i)
    print(cnt)