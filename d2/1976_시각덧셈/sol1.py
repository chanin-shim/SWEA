import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):

    numbers_list = list(map(int, input().split()))
    # print(numbers_list)
    # [3, 17, 1, 39]

    hour_list = []
    minute_list = []
    for i in range(len(numbers_list)):
        if i % 2 == 0:
            hour_list.append(numbers_list[i])
        else:
            minute_list.append(numbers_list[i])

    # print(hour_list, '  ', minute_list)
    # [3, 1][17, 39]

    hour_sum = 0
    for i in hour_list:
        hour_sum += i

    minute_sum = 0
    for i in minute_list:
        minute_sum += i

    if minute_sum >= 60:
        hour_sum += minute_sum // 60
        minute_sum = minute_sum % 60

    if hour_sum >= 13:
        while hour_sum >=13:
            hour_sum -= 12

    print("#{} {} {}".format(tc, hour_sum, minute_sum))
