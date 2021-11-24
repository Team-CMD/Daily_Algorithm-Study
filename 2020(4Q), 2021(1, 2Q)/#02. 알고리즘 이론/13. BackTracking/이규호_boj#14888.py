def Oper(result, index, operator):
    global value
    global N
    if index == len(N):
        value.append(result)
        return 0
    else:
        for i in range(len(operator)):
            before = result
            if i == 0 and operator[i] > 0:
                result += N[index]
            elif i == 1 and operator[i] > 0:
                result -= N[index]
            elif i == 2 and operator[i] > 0:
                result *= N[index]
            elif i == 3 and operator[i] > 0:
                if result < 0:
                    result = -result // N[index]
                    result = -result
                else:
                    result = result // N[index]
            else:
                continue
            operator[i] -= 1
            Oper(result, index+1, operator)
            result = before
            operator[i] += 1
    return


Num = int(input())
value = []
N = list(map(int, input().split()))
tmp = list(map(int, input().split()))
Oper(N[0], 1, tmp)
print(max(value))
print(min(value))