def solution(lottos, win_nums):
    min, max = 0, 0
    for i in win_nums:
        for j in lottos:
            if i == j:
                min += 1
    max = min + lottos.count(0)
    print(max, min)
    if min < 2 and max > 2:
        answer = [7-max, 6]
    elif max < 2 and min < 2:
        answer = [6, 6]
    else:
        answer = [7-max, 7-min]
    return answer
