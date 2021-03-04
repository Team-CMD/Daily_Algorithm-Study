n, m = map(int, input().split())
check_list = [False]*n
res = []

def backTracking(depth):
    if depth == m:
        print(' '.join([str(x) for x in res]))
        return
    for i in range(n):
        if check_list[i]:
            continue
        check_list[i] = True
        res.append(i+1)
        backTracking(depth+1)
        res.pop()
        for j in range(i+1, n):
            check_list[j] = False

if __name__ == '__main__':
    backTracking(0)