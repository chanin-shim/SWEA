import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):

    N, M = map(int, input().split())
    # print(N, M)
    # 5 3
    my_list = []

    for i in range (N):
        my_list += [list(map(int,input().split()))]

    #가로 확인
    ans_list = []
    for i in range(N): #0~4
        for j in range(N-M+1): # 0~4
                ans_list += [my_list[i][j:j+M]]
    # print(ans_list)
    # [[0, 0, 1], [0, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1],
    #  [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 0], [1, 0, 1]]

    result = 0
    for i in range(len(ans_list)):
        sumsum = 0
        for j in range(len(ans_list[i])):
            sumsum += ans_list[i][j]
            if sumsum == 0:
                result += 1

    print(result)

    #
    #         if my_list[i][j] or j == N -1:
    #             #벽을 만났을 때 그동안 쌓아온 cnt값이 K이면 들어갈 수 있다.
    #             if cnt == K:
    #                 ans += 1
    #             cnt = 0
    #     #열을 검사
    #     for j in range(N):
    #         if my_list[j][i] == 1:
    #             cnt += 1
    #         if my_list[j][i] == 0 or j == N -1:
    #             if cnt = K:
    #                 ans += 1
    #             cnt = 0
    #
    #
    #
    # print("#{} ".format(tc, ))