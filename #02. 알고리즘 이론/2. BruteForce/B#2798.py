N, M = map(int, input().split())
A = list(map(int, input().split()))
tmp1 = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            tmp2 = A[i] + A[j] + A[k]
            if (tmp1 < tmp2) and (tmp2 <= M):
                tmp1 = tmp2
print(tmp1)