N = int(input())
A = []

for i in range(N):
    a, b = map(int, input().split())
    a = a + b
    A.append(a)

for i in range(N):
    print(A[i])