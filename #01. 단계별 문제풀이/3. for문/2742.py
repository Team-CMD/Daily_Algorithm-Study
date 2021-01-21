N = input()
N = int(N)
a = []

for i in range(1, N + 1):
    a.append(i)

a.reverse()

for i in range(N):
    print(a[i])

N = input()
N = int(N)

for i in range(N):
    print(N - i)

N = int(input())

for i in range(N, 0, -1):
    print(i)