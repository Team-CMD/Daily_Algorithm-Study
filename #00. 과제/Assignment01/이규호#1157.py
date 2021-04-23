a = []
result = 0
alp = input()
alp = alp.lower()

for i in range(97, 123):
    a.append(alp.count(chr(i)))

for i in range(len(a)):
    if result < a[i]:
        result = a[i]
        index = i

if a.count(result) > 1:
    print("?", end="")
else:
    print(chr(65+index), end="")