N = int(input())
val = []
val_x = []
val_y = []
for _ in range(N):
    val.append(list(map(int, input().split())))
    # tmp = list(map(int, input().split()))
    # val_x.append(tmp[0])
    # val_y.append(tmp[1])
val.sort()
for i in range(N):
    print(val[i][0], val[i][1])