def PBNC(n):
    if n == 1:
        return 1

    if n == 0:
        return 0

    return PBNC(n-1)+PBNC(n-2)

if __name__=="__main__":
    print(PBNC(int(input())))