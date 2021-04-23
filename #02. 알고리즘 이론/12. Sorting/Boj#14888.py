from itertools import permutations #순열함수

def calc(numbers, oper, N):
    # Definition variable
    res = 0
    operC = 1
    ans = []
    # Substitue numbers for each operator type so as not to be duplicated
        # ex) input value of operator is '1 2 1 1',
        # The 'oper_set' list is saved 1, 2, 2, 3, 4 
    oper_list = []
    for j in range(len(oper)):
        oper_list += [operC]*oper[j]
        operC += 1
    
    oper_set = []
    for num in list(permutations(oper_list)):
        oper_set.append(num)
    oper_set = list(set(oper_set))

    # Divide the number of casese according to the operator type.
    for case in oper_set:
        # setting default value(=first value)
        res = numbers[0]

        for j in range(N-1):
            if case[j] == 1:
                res += numbers[j+1]
            elif case[j] == 2:
                res -= numbers[j+1]
            elif case[j] == 3:
                res *= numbers[j+1]
            elif case[j] == 4:#Belong to division rules
                if (res < 0):
                    res=-(-res//numbers[j+1])
                else:
                    res//=numbers[j+1]
        ans.append(res)
    print(max(ans))
    print(min(ans))

if __name__ == '__main__':
    N = int(input())
    numbers = list(map(int, input().split()))
    oper = list(map(int, input().split()))

    calc(numbers, oper, N)