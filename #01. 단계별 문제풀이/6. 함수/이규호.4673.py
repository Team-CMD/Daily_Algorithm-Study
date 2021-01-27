A = []
B = []
N = []


def self_num(num):
    NUM = list(str(num))
    for i in range(0, len(NUM)):
        NUM[i] = int(NUM[i])
        if num < 10000:
            num = num + NUM[i]
    return num


for i in range(1, 10000):
    A.append(i)
    N.append(self_num(i))

A = set(A)
N = set(N)
B = sorted(A - N)

for i in range(len(B)):
    print(B[i])