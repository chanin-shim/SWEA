import sys
sys.stdin = open("input.txt")

T = int(input())

# 시계방향
dr = [0,1,0,-1]
dc = [1,0,-1,0]

for tc in range(1, T + 1):
    N = int(input())

    # N*N 리스트 만들기
    snail = [[0] * N for _ in range(N)]
    # print(snail)
    # [[0, 0], [0, 0]] 2 1 1
    # [[0, 0, 0], [0, 0, 0], [0, 0, 0]] 3 2 2 1 1
    # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] 4 3 3 2 2 1 1
    # [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]] 5 4 4 3 3 2 2 1 1

    d = 0
    row = 0
    col = 0

    for i in range (1, N*N+1):
        if row == N or col == N or snail[row][col] != 0 :
            row -= dr[d]
            col -= dc[d]
            d += 1
            if d == 4:
                d = 0
            row += dr[d]
            col += dc[d]

        # 왜 여기 부분 else 한거랑 안한거랑 답이 차이나는지?
        snail[row][col] = i
        row += dr[d]
        col += dc[d]

    # print(*snail)

    print("#{}".format(tc))
    for i in range(len(snail)):
        print(*snail[i])



        #