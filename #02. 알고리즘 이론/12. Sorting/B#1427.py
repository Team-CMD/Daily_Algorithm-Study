N = list(input())
transform = list(map(int, N))
transform.sort(reverse=True)
for i in range(len(transform)):
    print(transform[i], end='')