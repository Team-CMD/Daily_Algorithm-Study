# 소수 만들기

def solution(nums):
    answer = 0
    tmp = []

    for i in range(len(nums)):
        tmp1 = 0
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                for l in range(2, nums[i]+nums[j]+nums[k]):
                    if (nums[i]+nums[j]+nums[k]) % l == 0:
                        tmp1 = 1
                        break
                    else:
                        tmp1 = 0
                if tmp1 == 0:
                    tmp.append(nums[i]+nums[j]+nums[k])

    return len(tmp)
