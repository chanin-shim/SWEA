import sys
sys.stdin = open('input.txt')

T = int(input())

# 3x3용
dr_33 = [-3,-3,0,3,3,3,0,-3]
dc_33 = [0,3,3,3,0,-3,-3,-3]

# 상 우상 우 우하 하 좌하 좌 좌상
dr_8 = [-1,-1,0,1,1,1,0,-1]
dc_8 = [0,1,1,1,0,-1,-1,-1]

for tc in range(1,T+1):
    N = 9
    my_list =  [list(map(int,input().split())) for _ in range(N)]

    # print(my_list)
    # [
    # [7, 3, 6, 4, 2, 9, 5, 8, 1],
    # [5, 8, 9, 1, 6, 7, 3, 2, 4],
    # [2, 1, 4, 5, 8, 3, 6, 9, 7],
    # [8, 4, 7, 9, 3, 6, 1, 5, 2],
    # [1, 5, 3, 8, 4, 2, 9, 7, 6],
    # [9, 6, 2, 7, 5, 1, 8, 4, 3],
    # [4, 2, 1, 3, 9, 8, 7, 6, 5],
    # [3, 9, 5, 6, 7, 4, 2, 1, 8],
    # [6, 7, 8, 2, 1, 5, 4, 3, 9]
    # ]


    result = 0
    # 가로확인
    for i in range(N):
        my_set = set()
        for j in range(N):
            my_set.add(my_list[i][j])
            if len(my_set) == 9:
                result = 1

    # 세로확인
    for i in range(N):
        my_set = set()
        for j in range(N):
            my_set.add(my_list[j][i])
            if len(my_set) == 9:
                result = 1

    core = my_list[5][5]
    for i in range(8):
        nr = [5] + dr_33
        nc = [5] + dc_33
        my_set_2 = set()
        for j in range(8):
            nr_2 = nr + dr_8
            nc_2 = nc + dc_8
            print(nr_2,'   ',nc_2)
            # my_set_2.add(my_list[nr_2[0]][nc_2][0])
            # print(my_set_2)

