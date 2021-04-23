import sys

def Take(Stack:list, u:str):
    if u[0] == 'push':
        Stack.append(int(u[1]))
    elif u[0] == 'pop':
        if len(Stack) == 0:
            print(-1)
        else:
            print(Stack.pop())
    elif u[0] == 'size':
        print(len(Stack))
    elif u[0] == 'empty':
        if len(Stack) == 0:
            print(1)
        else:
            print(0)
    elif u[0] == 'top':
        if len(Stack) == 0:
            print(-1)
        else:
            print(Stack[-1])
    
    return 0

if __name__ == '__main__':
    S = []
    n = int(sys.stdin.readline())
    for _ in range(n):
        order = sys.stdin.readline().split()
        Take(S, order)