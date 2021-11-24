from itertools import permutations

cal = 0 # 0:+, 1:- 2:*, 3://
N = int(input())
arr_num = list(map(int, input().split()))
arr_cal_num = list(map(int, input().split()))

# 연산자 리스트 만들기
arr_cal = []
for i in arr_cal_num:
    arr_cal += [cal]*i
    cal += 1

# 조합 을 이용해 중복없는 리스트 만들기
arr_cal_set = set(permutations(arr_cal))

# 각 숫자별 계산
tmp_arr = []
for arr_cal_set_num in arr_cal_set:
    tmp = arr_num[0]
    for i in range(N-1):
        if arr_cal_set_num[i] == 0:
            tmp += arr_num[i+1]
        elif arr_cal_set_num[i] == 1:
            tmp -= arr_num[i+1]
        elif arr_cal_set_num[i] == 2:
            tmp *= arr_num[i+1]
        elif arr_cal_set_num[i] == 3:
            if tmp < 0:
                tmp = -(-tmp // arr_num[i+1])
            else:
                tmp //= arr_num[i+1]
    tmp_arr.append(tmp)

print(max(tmp_arr))
print(min(tmp_arr))     

        



