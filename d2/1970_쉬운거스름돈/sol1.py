import sys
sys.stdin = open("input.txt")

T = int(input())

money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
# 가장 큰 값으로 부터 나누고, 내림차순으로 하나씩 나눠줌.
# 나눠지는 값이 0이 되면 멈추기.

for tc in range(1, T+1):

    N = int(input())
    cnt_list = []
    [cnt_list.append(0) for _ in range(len(money_list))]
    # print(cnt_list)
    # [0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(money_list)):
        while N >= money_list[i]:
            cnt_list[i] += N // money_list[i]
            N = N % money_list[i]

    print("#{}".format(tc))
    for i in cnt_list:
        print(i, end=" ")
    print(" ")