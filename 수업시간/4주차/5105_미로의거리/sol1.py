import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):

    N = int(input())

    my_list = [list(map(int,input()))for _ in range(N)]

    print(my_list)
    # [
    # [1, 3, 1, 0, 1],
    # [1, 0, 1, 0, 1],
    # [1, 0, 1, 0, 1],
    # [1, 0, 1, 0, 1],
    # [1, 0, 0, 2, 1]
    # ]

    start_row = 0
    start_col = 0
    end_row = 0
    end_col = 0
    for i in range(N):
        for j in range(N):
            if my_list[i][j] == 2:
                start_row = i
                start_col = j
    for i in range(N):
        for j in range(N):
            if my_list[i][j] == 3:
                end_row = i
                end_col = j




    print("#{} ".format(tc, ))