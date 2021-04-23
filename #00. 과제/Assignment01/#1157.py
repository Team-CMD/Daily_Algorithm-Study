string = list(input())
Ascii = []
Max_check = []

for i in string:
    if ord(i) > 96:
        Ascii.append(ord(i)-32)
    else:
        Ascii.append(ord(i))

for i in range(65,91):
    Max_check.append((Ascii.count(i)))

if Max_check.count(max(Max_check)) > 1:
    print('?')
else:
    tmp = Max_check.index(max(Max_check)) # 최대 빈도로 나타나는 알파벳의 인덱스
    print(chr(tmp+65))









