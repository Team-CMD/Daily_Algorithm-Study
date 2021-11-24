N = int(input())
count = 0

for i in range(N):
    Word = []
    tmp = 0
    Word = input()

    for j in range(len(Word)):
        if Word.count(Word[j]) > 1:
            if tmp != 2:
                tmp = 0
            for k in range(1, len(Word)-j):
                if Word[j] == Word[j+k]:
                    if tmp == 1:
                        tmp = 2
                        break
                    continue
                elif tmp != 2 and Word[j] != Word[j+k]:
                    tmp = 1
    if tmp != 2:
        count += 1

print(count)