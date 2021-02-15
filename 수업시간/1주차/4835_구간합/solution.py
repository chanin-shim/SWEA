T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 원소의 갯수 = N
    # 구간의 길이 = M

    max_value = 0
    min_value = 23129214124

    # 구간 시작점
    for i in range(N - M + 1):
        tmp = 0

        for j in range(M):
            tmp += nums[i + j]
        # for j in nums[i:i+M]
        #     tmp += j
        # 위와 같음

        if max_value < tmp:
            max_value = tmp

        if min_value > tmp:
            min_value = tmp

    print("#{} {}".format(tc, max_value - min_value))
#######################################################################################################################

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 원소의 갯수 = N
    # 구간의 길이 = M
    nums = list(map(int,input().split()))

    max_value = 0
    min_value = 23129214124

    # 중복된 연산을 피하자....

    tmp = 0
    for i in range(M):
        tmp += nums[i]

    max_value = tmp
    min_value = tmp

    for i in range(M, N):
        tmp = tmp + nums[i] - nums[i - M]

        if max_value < tmp:
            max_value = tmp

        if min_value > tmp:
            min_value = tmp

    # print("#{} {}".format(tc, max_value-min_value))


# 컨트롤 알트 엘 누르면 정렬됨 띄어쓰기랑