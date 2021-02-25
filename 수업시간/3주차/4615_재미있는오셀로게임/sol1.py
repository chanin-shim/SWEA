import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N, M = map(int,input().split())
    # print(N,M)
    # 4 12
    # N = N*N 보드길이
    # M = 돌을 놓는 횟수

    my_board = [['X' for _ in range (N+2)]for _ in range (N+2)]

    # print(my_board)
    # [['X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X']]

    half = N//2
    my_board[half][half] = 'W'
    my_board[half][half+1] = 'B'
    my_board[half+1][half] = 'B'
    my_board[half+1][half+1] = 'W'


    for i in range(M):
        x,y,color = map(int,input().split())
        if color == 1:
            my_board[x][y] = 'B'
        if color == 2:
            my_board[x][y] = 'W'

        for j in range(N):
            for k in range(N):
                cnt_1 = 0
                cnt_2 = 0
                cnt_diag_1 = 0
                cnt_diag_2 = 0

                # 상하좌우
                # 상
                if my_board[j][k+1] == 'B':
                    cnt_1 += 1
                if my_board[j][k+1] == 'W':
                    cnt_2 += 1

                #하
                if my_board[j][k-1] == 'B':
                    cnt_1 += 1
                if my_board[j][k-1] == 'W':
                    cnt_2 += 1

                #좌
                if my_board[j-1][k] == 'B':
                    cnt_1 += 1
                if my_board[j-1][k] == 'W':
                    cnt_2 += 1

                #우
                if my_board[j+1][k] == 'B':
                    cnt_1 += 1
                if my_board[j+1][k] == 'W':
                    cnt_2 += 1

                if cnt_1 == 3 or cnt_2 == 3:
                    if cnt_1 > cnt_2: #흑으로 둘러쌓였다면
                        my_board[j][k] == 'B'
                    else:
                        my_board[j][k] == 'W'

                #대각선
                if my_board[j+1][k+1] == 'B':
                    cnt_diag_1 += 1
                if my_board[j+1][k+1] == 'W':
                    cnt_diag_2 += 1

                if my_board[j+1][k-1] == 'B':
                    cnt_diag_1 += 1
                if my_board[j+1][k-1] == 'W':
                    cnt_diag_2 += 1

                if my_board[j-1][k+1] == 'B':
                    cnt_diag_1 += 1
                if my_board[j-1][k+1] == 'W':
                    cnt_diag_2 += 1

                if my_board[j-1][k-1] == 'B':
                    cnt_diag_1 += 1
                if my_board[j-1][k-1] == 'W':
                    cnt_diag_2 += 1

                if cnt_diag_1 % 2 == 0 or cnt_diag_2 % 2 == 0:
                    if cnt_diag_1 > cnt_diag_2:
                        my_board[j][k] == 'B'
                    if cnt_diag_2 > cnt_diag_1:
                        my_board[j][k] == 'W'
                    # if cnt_diag_2 == 2 and cnt_diag_1 == cnt_diag_2:
                        # 이거 조건을 못주겠다.

                # for 문 전체 돌려서, 현재있는 것중에 3개에 둘러쌓인거 바꿔주기


    print(my_board)
    # [['X', 'X', 'X', 'X', 'X', 'X'],
    #  ['X', 'W', 'B', 'W', 'W', 'X'],
    #  ['X', 'B', 'W', 'B', 'B', 'X'],
    #  ['X', 'W', 'B', 'W', 'B', 'X'],
    #  ['X', 'W', 'W', 'B', 'W', 'X'],
    #  ['X', 'X', 'X', 'X', 'X', 'X']]


    cnt_W = 0
    cnt_B = 0
    for i in range(len(my_board)):
        for j in range(len(my_board)):
            if my_board[i][j] == 'W':
                cnt_W += 1
            if my_board[i][j] == 'B':
                cnt_B += 1

    print("#{} {} {}".format(tc,cnt_B,cnt_W))



    # if (my_board[x - 2][y] == 'B' and my_board[x - 1][y] == 'W') or (
    #         my_board[x][y - 2] == 'B' and my_board[x][y - 1] == 'W') \
    #         or (my_board[x + 2][y] == 'B' and my_board[x + 1][y] == 'W') or (
    #         my_board[x][y + 2] == 'B' and my_board[x][y + 1] == 'W') \
    #         or (my_board[x - 2][y - 2] == 'B' and my_board[x - 1][y - 1] == 'W') or (
    #         my_board[x + 2][y + 2] == 'B' and my_board[x + 1][y + 1] == 'W'):
