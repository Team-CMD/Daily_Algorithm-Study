#승현
A = int(input())
for i in range(A):
    lis = list(map(str, input()))
    count = 0
    an = 0
    for j in range(len(lis)):
        if lis[j] == 'O':
            count+=1
            an+=count
        else:
            count = 0
    print(an)

'''
#민준
N = int(input())

for i in range(N):
    score = 0
    tmp = 0
    arr = list(input())
    for j in range(len(arr)):
        if arr[j] == 'O':
            tmp += 1
            score += tmp
        else:
            tmp = 0
        
    print(score)

# 병근 답
N = int(input())
list = []
list2 = []
num = 1
hap = 0
for i in range(N):
    C = input("")
    for j in range(len(C)):
        if C[j] == "o":
            list.append(1)
        elif C[j] == "x":
            list.append(0)
    for h in range(len(list)):
        if list[h] == 1:
            list2.append(num)
            num = num + 1
        else :
            list2.append(0)
            num = 1
    for k in range(len(list2)):
        hap = hap + list2[k]
    print(hap)
    list = []
    list2 = []
    hap = 0

#형순
case = int(input())
score = 0

for i in range (0,case):
    answer = input()
    count = 1
    score = 0
    for j in range (0,len(answer)):
        if(answer[j] == "o"):
            score = score + count
            count += 1
        else:
            count = 1
    print(score)


'''
    
    
            


    

