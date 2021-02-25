# 체스판

# M * N 크기의 board
# 체스판 크기 : 8 * 8 (64개 칸)
#     검은색, 흰색이 번갈아가면서 칠해져있다.
#         > 각 간이 W, B중 하나로 색칠해야 함
#         > 이웃하는 두개의 칸은 서로 다른 색

# W B W B W B W B 
# B W B W B W B W 
# W B W B W B W B 
# B W B W B W B W 
# W B W B W B W B 
# B W B W B W B W 
# W B W B W B W B 
# B W B W B W B W  

# B W B W B W B W
# W B W B W B W B
# B W B W B W B W
# W B W B W B W B
# B W B W B W B W
# W B W B W B W B
# B W B W B W B W
# W B W B W B W B

# >> M * N 크기의 보드 가운데 8*8 크기의 정사각형을 뽑아내서
# 체스판처럼 색칠한다. 최소개수의 색칠하는 칸

def initChessBoard(W, B):
    init=[W, B]
    chess = []
    unit = []
    trig = 0
    for _ in range(8):
        unit = []
        if trig == 0:
            unit.append(init[0])
            for _ in range(3):
                unit.append(init[1])
                unit.append(init[0])
            unit.append(init[1])
            trig += 1
        elif trig == 1:
            unit.append(init[1])
            for _ in range(3):
                unit.append(init[0])
                unit.append(init[1])
            unit.append(init[0])
            trig -= 1
        chess.append(unit)

    return chess

if __name__ == '__main__':
    white_board = initChessBoard('w','b')
    black_board = initChessBoard('b','w')
    n,m = map(int,input().split())
    board = []
    result = []
    for i in range(n):
        wb = list(map(str,input()))
        board.append(wb)

    for j in range(m-7):
        q = 0
        w = 0
        for k in range(n-7):
            count_black = 0
            count_white = 0
            for l in range(j,j+8):
                for x in range(k,k+8):
                    if board[x][l] != white_board[q][w]:
                        count_white +=1
                        if board[x][l] != black_board[q][w]:
                            count_black +=1
                        w+=1
                    w = 0
                    q+=1
                q = 0
                result.append(count_black)
                result.append(count_white)
    print(min(result))

