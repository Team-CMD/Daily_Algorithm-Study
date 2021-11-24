li = []
for _ in range(int(input())):
    li.append(int(input()))

chk = sorted(li)
for i in range(len(li)):
    print(chk[i])