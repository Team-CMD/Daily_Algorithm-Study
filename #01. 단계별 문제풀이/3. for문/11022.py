N = int(input())
R = []
A = []
B = []

for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    a = a + b
    R.append(a)

for i in range(N):
    print("Case #%d: %d + %d = %d" %(i+1, A[i], B[i], R[i]))