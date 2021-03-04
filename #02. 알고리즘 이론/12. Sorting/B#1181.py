import sys

li = []
for _ in range(int(input())):
    tmp = sys.stdin.readline()
    li.append(tmp[:-1])
temp = set(li)
work = list(temp)
for i in range(0, len(work)):
    print(sorted(work[i]))