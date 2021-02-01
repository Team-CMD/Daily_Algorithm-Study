def un_limit(string):
    return string * 2


def compare(s1, t1):
    j = 0
    S1 = un_limit(s1)
    T1 = un_limit(t1)

    if len(s1) > len(t1):
        for i in range(len(S1)):
            if S1[i] == t1[j]:
                j += 1
                if j == (len(t1)):
                    j = 0
                continue
            else:
                return 0
        return 1
    elif len(s1) < len(t1):
        for i in range(len(T1)):
            if s1[j] == T1[i]:
                j += 1
                if j == (len(s1)):
                    j = 0
                continue
            else:
                return 0
        return 1
    else:
        for i in range(len(S1)):
            if S1[i] == T1[i]:
                continue
            else:
                return 0
        return 1


if __name__ == "__main__":
    s = list(input())
    t = list(input())
    print(compare(s, t))