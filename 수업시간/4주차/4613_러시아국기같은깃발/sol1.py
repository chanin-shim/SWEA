import sys
sys.stdin = open("input.txt")

T = int(input())





for tc in range(1, T+1):

    N, M = map(int, input().split())
    my_flag = [list(map(str,input()))for _ in range (N)]
    # print(N,M , ' ', my_flag)
    # 4 5
    # [
    # ['W', 'R', 'W', 'R', 'W'],
    # ['B', 'W', 'R', 'W', 'B'],
    # ['W', 'R', 'W', 'R', 'W'],
    # ['R', 'W', 'B', 'W', 'R']
    # ]

    W_cnt = 0
    B_cnt = 0
    R_cnt = 0

    ans = 0

    WBR_count = [[] for _ in range (N)]
    for i in range(N):
        W_cnt = 0
        B_cnt = 0
        R_cnt = 0
        for j in range(M):
            if my_flag[i][j] == 'W':
                W_cnt += 1
            if my_flag[i][j] == 'B':
                B_cnt += 1
            if my_flag[i][j] == 'R':
                R_cnt += 1
        WBR_count[i] += W_cnt,B_cnt,R_cnt

    # print(WBR_count)
    # [[3, 0, 2], [2, 2, 1], [3, 0, 2], [2, 1, 2]]

    # 일단 1번째는 W, 마지막은 R가 반드시 돼야함
    for i in range(len(WBR_count)):
        for j in range(len(WBR_count[0])):
            WBR_count[i][j]

    abs +=  (5 - WBR_count[0][0])


    print("#{} ".format(tc, ))