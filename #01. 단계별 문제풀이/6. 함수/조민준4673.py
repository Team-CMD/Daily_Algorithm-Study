def d(n):
    tmp = 0 
    for i in list(str(n)):
        tmp += int(i)
    return tmp + int(n)
if __name__ == "__main__":
    NonSelf_Number = []
    Number = []

    for i in range(1,10001): 
        Number.append(i)

    for i in range(1,10001):
        NonSelf_Number.append(d(i))

    Number_sub_NonSelf_Numer = [x for x in Number if x not in NonSelf_Number]

    for i in range(len(Number_sub_NonSelf_Numer)):
        print(Number_sub_NonSelf_Numer[i]) 