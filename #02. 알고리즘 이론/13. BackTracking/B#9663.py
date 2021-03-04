BOJ 9663
BackTracking "N - Queen"
체스판 -> size ( N * N )
    N개의 퀸을 놓는다.
    > 퀸의 이동경로 ( 가로, 세로, 대각선 )
    퀸을 놓았을 때 서로의 퀸이 공격할 수 없다.
        => 서로의 퀸은 이동경로가 겹치지 않는다.

>> 서로의 퀸이 이동경로가 겹치지 않는 경우의 수

주어지는 값 ) N값.
입력 형태 ) 첫째줄에 N이 주어짐. ( 1 <= N < 15 )
출력 형태 ) 첫째줄에 구하고자 하는 경우의 수 출력

-------------------------------------------------------------------

> 의견을 많이 주고받는다.
> 해당 문제의 풀이방법을 정해야 함.
> 4명이서 문제를 푸는것.
    -> 의견수합이 가장 효율적으로 이루어져야 함.

[Solution]
    1. Python 
        0) N을 입력받음.
            N = int(input())
        1) N*N 체스판을 만든다.
            1-1) list를 활용하여 체스판을 만든다.
            > Bord = [[0 for _ in range(N)] for  in range(N)]
            1-2) 초깃값 = 0, Q의 위치= 1, Q의 동선 = 2 
        2) 1번째 Q의 이동경로를 체크. -> 함수()
            2-1) i번째 Q를 (0,0)에 위치. (i=1)
                2-2) i번째 Q의 동선을 체크
                2-3) 체스판을 순회해서 가장 가까운 0의 위치를 탐색
                     (예외처리 참조)
                2-4) (2-3)에서 찾은 위치에 (i+1)번째 Q를 위치시킨다.
        3) 2)를 N개의 Q이 놓일때까지 반복.

        예외처리)
            N*N 크기의 체스판에서 N개의 퀸이 안들어갈 경우

# def moveCheck(n, board, i, j, cnt):
#     if board[i][j] == 1:
#         for a in range(n):
#             if (i!=a) and (j!=a):
#                 board[i][a] = 2
#                 board[a][j] = 2
#                 if (i+a)<n and (j+a)<n:
#                     board[i+a][j+a] = 2
#                 if (a-i)<n and (a-j)<n:
#                     board[a-i][a-j] = 2
#     for x in range(n):
#         for y in range(n):
#             if board[x][y] == 1:
#                 cnt += 1

# def nQueen(n, board):
#     cnt = 0
#     res = 0
#     for i in range(1, n+1):
#         if i==1:
#             board[0][0] = 1
#             moveCheck(n, board, 0, 0, cnt)
#             print("present board is {0}".format(board))
#         for a in range(n):
#             for b in range(n):
#                 if board[a][b] == 0:
#                     board[a][b] == 1
#                     moveCheck(n, board, a, b, cnt)
#                     print("present board is {0}".format(board))
#         print("cnt is {0}".format(cnt))
#     if cnt == n:
#         res += 1
#     return res

# if __name__=='__main__':
#     N = int(input())
#     global cnt, res
#     board = [[0 for _ in range(N)] for _ in range(N)]
#     result = nQueen(N, board)
#     print(result)