#재훈
def calc_mean(n, m, s):
    re_s = [0]*n
    tmp = 0
    for i in range(n):
        re_s[i] = s[i]/m*100
        tmp += re_s[i]
    result = tmp/n
    print(result)

if __name__ == '__main__':
    N = int(input())
    score = list(map(int, input().split()))
    M = max(score)
    calc_mean(N, M, score)

'''
#민준
N = int(input())
Before_score = list(map(int, input().split()))
tmp = (sum(Before_score)/N)/max(Before_score)*100
print(tmp)

'''

    

    
    
