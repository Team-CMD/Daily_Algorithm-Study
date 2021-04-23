import sys

if __name__ == '__main__':
    pallet = [1,2,3,4,5,6,7,8,9]
    check = [0]*9
    map = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

    for _ in range(2):
        for i in range(9):
            # 가로줄의 빈칸이 1개일 경우 가로줄을 체크한다.
            # 스도쿠를 전치시켜서 다시 가로줄을 체크한다. ( = 세로줄을 체크하는것 )
            # 이후 결과가 가로세로 모두 한줄에 0이 2개인경우만 남는다.
            if map[i].count(0) == 1:
                for j in range(9):
                    if map[i][j] in pallet:
                        check[map[i][j]-1] = 1
                    else:
                        tmp = j
                map[i][tmp] = pallet[check.index(0)]
                check = [0]*9

        # 보드를 전치시킨다.
        map = [list(x) for x in zip(*map)]

    for j in range(9):
        print(map[j])
    # 작은 정사각형 체크해야함.
    row_start = 0
    col_start = 0
    row_num = 3
    col_num = 3
    for _ in range(3):
        square = []
        square_ind = [0, 0]
        for j in range(row_start, row_num):
            for k in range(col_start, col_num):
                if map[j][k] == 0:
                    square_ind[0], square_ind[1] = j, k
                    square.append(map[j][k])
                else:
                    square.append(map[j][k])
            col_start += 3
            col_num += 3
        square.sort()

        for a in range(9):
            if pallet[a] not in square:
                map[square_ind[0]][square_ind[1]] = pallet[a]

        row_start += 3
        row_num += 3

#=====================================================================================
sudoku = [list(map(int, input().split())) for _ in range(9)]
#해결해야될 칸만 받음
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

def is_promising(i, j):
    promising = [1,2,3,4,5,6,7,8,9]  
    
    #행열 검사
    for k in range(9):
        if sudoku[i][k] in promising:
            promising.remove(sudoku[i][k])
        if sudoku[k][j] in promising:
            promising.remove(sudoku[k][j])
            
    #3*3 박스 검사
    i //= 3
    j //= 3
    for p in range(i*3, (i+1)*3):
        for q in range(j*3, (j+1)*3):
            if sudoku[p][q] in promising:
                promising.remove(sudoku[p][q])
    
    return promising

flag = False #답이 출력되었는가?
def dfs(x):
    global flag
    
    if flag: #이미 답이 출력된 경우
        return
        
    if x == len(zeros): #마지막 0까지 다 채웠을 경우
        for row in sudoku:
            print(*row)
        flag = True #답 출력
        return
        
    else:    
        (i, j) = zeros[x]
        promising = is_promising(i, j) #유망한 숫자들을 받음
        
        for num in promising:
            sudoku[i][j] = num #유망한 숫자 중 하나를 넣어줌
            dfs(x + 1) #다음 0으로 넘어감
            sudoku[i][j] = 0 #초기화 (정답이 없을 경우를 대비)
dfs(0)    