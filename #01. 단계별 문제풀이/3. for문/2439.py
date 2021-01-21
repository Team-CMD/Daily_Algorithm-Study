N = int(input())

for i in range(N, 0, -1):
    # print("/"*i)
    for j in range(i-1):
        print(" ", end="")
    for j in range(N - i + 1, 0, -1):
        print("*", end="")
    print("")