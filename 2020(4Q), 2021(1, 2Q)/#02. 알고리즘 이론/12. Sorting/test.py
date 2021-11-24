import sys

if __name__ == '__main__':
    pallet = [1,2,3,4,5,6,7,8,9]
    trig = 1
    check = [0]*9
    map = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

    for _ in range(2):
        for i in range(9):
            #가로줄의 빈칸이 1개일 경우 가로줄을 체크한다.
            #스도쿠를 전치시켜서 다시 가로줄을 체크한다. ( = 세로줄을 체크하는것 )
            # 이후 결과가 한줄에 0이 2개인경우만 남는다.
            if map[i].count(0) == 1:
                for j in range(9):
                    if map[i][j] in pallet:
                        check[map[i][j]-1] = 1
                    else:
                        tmp = j
                map[i][tmp] = pallet[check.index(0)]
                check = [0]*9

        map = [list(x) for x in zip(*map)]
        
    # 작은 정사각형 체크해야함.
    for i in range(9):
        for j in range(9):
            
    # test = [2,5,1,6,0,8,9,3,7]
    # for k in range(9):
    #     if test[k] in pallet:
    #         print('Yes ', test[k])
    #         check[test[k]-1] = 1
    #     else:
    #         print('No, ', test[k])
    # # [2, 5, 1, 6, 0, 8, 9, 3, 7]
    # # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # # [1, 1, 1, 0, 1, 1, 1, 1, 1]
    for j in range(9):
        print(map[j])