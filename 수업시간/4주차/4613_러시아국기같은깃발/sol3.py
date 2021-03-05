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
    R_cnt = 0
    B_cnt = 0

    total_count = [W_cnt,R_cnt,B_cnt]
    for i in range(N):
        total_count[0] = 0
        total_count[1] = 0
        total_count[2] = 0
        for j in range(M):
            if my_flag[i][j] == 'W':
                total_count[0] += 1
            if my_flag[i][j] == 'R':
                total_count[1] += 1
            if my_flag[i][j] == 'B':
                total_count[2] += 1
        print(total_count)

    print("#{} ".format(tc, ))