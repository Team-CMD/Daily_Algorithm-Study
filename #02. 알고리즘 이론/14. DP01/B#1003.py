for i in range(int(input())):
    pass

def fibonacci(n):
    cnt0 = 0
    cnt1 = 0
    if n==0:
        cnt0+=1
        return 0
    elif n==1:
        cnt1+=1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)