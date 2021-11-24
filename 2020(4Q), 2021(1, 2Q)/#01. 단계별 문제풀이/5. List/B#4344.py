#민준
C = int(input())

for i in range(C):
    Num_Score = list(map(int, input().split()))
    Avg = sum(Num_Score[1:]) / Num_Score[0]

    count = 0
    for j in Num_Score[1:]:
        if j > Avg:
            count += 1
        
    rate = (count / Num_Score[0])*100
    print('%0.3f' %round(rate,3) +'%')

'''

#승현
A = int(input())
for i in range(A):
    lis = list(map(int, input().split()))
    avr = 0.0
    count = 0
    ad = 0
    for j in range(1,len(lis)):
        ad += lis[j]

    avr = ad / (len(lis)-1)
    for j in range(1, len(lis)):
        if avr<lis[j]:
            count+=1
    tmp = 100*count/(len(lis)-1)
    print(format(tmp,".3f"),"%",sep='')


#형순
Test_case = int(input())

for i in range (0,Test_case):
    sum = 0
    count = 0
    aver = 0
    rate = float(0)
    score = list(map(int,input().split()))

   # aver = sum(score[1:len(score)-1]) / score[0]

    Std_num = score[0]
    for j in range (1,len(score)):
        sum += score[j]
    aver = sum / Std_num 

    for i in range (1, len(score)):
        if(aver < score[i]):
            count += 1
    rate = (count / Std_num) * 100

    print(format(rate, ".3f")+'%')


#병근
C = int(input(""))
A, averge = 0, 0
G = 0
for i in range(C):
    N = list(map(int, input().split(" ")))
    averge = sum(N) / N[0]
    G = 0
    for j in range(N[0]):
        if N[j+1] > averge :
            G = G + 1
    print("%0.3f"%((G/N[0])*100))


#규호형
N = int(input())
average = []

for i in range(N):
    count = 0
    Grade = 0
    grade = list(map(int, input().split()))
    for j in range(1, grade[0]):
        Grade = Grade + grade[j]
    Grade = Grade / grade[0]
    for j in range(grade[0]):
        if grade[j] > Grade:
            count += 1

    average.append((count / grade[0]) * 100)


for i in range(N):
    print("%0.3f%" % average[i])
'''
