import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    my_maze = [list(map(int,input()))for _ in range(N)]
    print(my_maze)
    # [
    # [1, 3, 1, 0, 1],
    # [1, 0, 1, 0, 1],
    # [1, 0, 1, 0, 1],
    # [1, 0, 1, 0, 1],
    # [1, 0, 0, 2, 1]
    # ]

    start_i = 0
    start_j = 0
    for i in range(N):
        for j in range(N):
            if my_maze[i][j] == 3:
                start_i = i
                start_j = j

    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    my_maze[start_i][start_j]




    print("#{} ".format(tc, ))