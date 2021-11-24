import sys

if __name__=='__main__':
    value = [0]*10001
    for i in range(int(input())):
        tmp = int(sys.stdin.readline())
        value[tmp] = value[tmp] + 1

    for i in range(10001):
        if value[i] != 0:
            for _ in range(value[i]):
                print(i)