# 병근 답
num = int(input("수 입력 : "))
new_num = num
count = 1
n1, n2, n3 = 0, 0, 0
if(num >= 10):
    n1 = num // 10
    n2 = num % 10
    n3 = n1 + n2
    if (n3 >= 10):
        n3 = n3 - 10
    else :
        pass
    num = n2*10 + n3
else :
    num = num*10 + num
while(num != new_num):
    if(num >= 10):
        n1 = num // 10
        n2 = num % 10
        n3 = n1 + n2
        if (n3 >= 10):
            n3 = n3 - 10
        else :
            pass
        num = n2*10 + n3
    else :
        num = num*10 + num
    count = count + 1
print(count)

# 백준 답 
tmp = inp = int(input())
count = 0
while True:
    ten = tmp//10
    one = tmp%10
    res = ten + one
    count += 1
    tmp = int(str(tmp%10)+str(res%10))
 
    if (inp==tmp):
        break
print(count)
