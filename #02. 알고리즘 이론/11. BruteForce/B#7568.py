if __name__=="__main__":
    # N값 입력
    # N명의 몸무게, 키 데이터 입력받음.
    # 2차원 리스트로 활용
    N = int(input())
    group = [list(map(int, input().split())) for _ in range(N)]
    
    #print(group)
    
    # 데이터를 순회반복하며 크기 비교 
    for j in range(N):
        rank = 1
        for k in range(N):
            if j == k:
                # 같은 대상 비교방지
                continue
            if (group[j][0] < group[k][0]) and (group[j][1] < group[k][1]):
                rank += 1
        print(rank, end=" ")