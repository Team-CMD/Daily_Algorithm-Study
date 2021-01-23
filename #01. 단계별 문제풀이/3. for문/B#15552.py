import sys
N = int(sys.stdin.readline())

A = []

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    a = a + b
    A.append(a)

for i in range(N):
    print(A[i])