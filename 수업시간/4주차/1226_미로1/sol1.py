import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    N = 16
    test_num = int(input())
    my_maze = [list(map(int,input()))for _ in range(N)]
    # print(my_maze)
    # [
    # [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    # [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
    # [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
    # [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1],
    for i in range(N):
        for j in range(N):
            if my_maze[i][j] == 2:
                start_row = i
                start_col = j
    for i in range(N):
        for j in range(N):
            if my_maze[i][j] == 3:
                end_row = i
                end_col = j
    # print((start_row,start_col),'->',(end_row,end_col))
    # (1, 1) -> (13, 13)

    #상하좌우
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    my_maze[start_row][start_col]

    visited = [[0]*N for _ in range(N)]

    visited[start_row][start_col] = 1 # 일단 들린걸로 함.

    for i in range(4):
        if 0 <= start_row + delta_row[i] < 16 and 0 <= start_col + delat_col[i] < 16 and visited


    print("#{} ".format(tc, ))