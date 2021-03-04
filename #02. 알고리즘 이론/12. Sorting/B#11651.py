N = int(input())
val = []
val_x = []
val_y = []
for i in range(N):
    # val.append(list(map(int, input().split())))
    tmp = list(map(int, input().split()))
    val_x.append(tmp[0])
    val_y.append(tmp[1])
    val.append([val_y[i], val_x[i]])
val.sort()
for i in range(N):
    print(val[i][1], val[i][0])