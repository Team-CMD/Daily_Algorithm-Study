def d(v):
    res = v
    for num in list(str(v)):
        res += int(num)
    return res

if __name__ == "__main__":
    Answer = [] # d(n)의 값을 집어넣을 예정

    for cnt in range(10001):
        Answer.append(d(cnt))

    Answer.sort()

    for cnt in range(1, 10000):
        if cnt in Answer: # None-SelfNumber
            continue
        else: # SelfNumber
            print(cnt)