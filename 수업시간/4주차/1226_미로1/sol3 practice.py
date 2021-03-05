import sys
sys.stdin = open("input.txt")

T = 10

def DFS (r,c):
    Q = [(r,c)]

    while Q:
        now_r, now_c = Q.pop(0)
        for i in range(4):
            nr = now_r + dr[i]
            nc = now_c + dc[i]

            if 0<=nr<16 and 0<=nc<16:
                if maze[nr][nc] == 3:
                    return 1
            # 갈 수 있는 자리라면
            if maze[nr][nc] != 1:
                Q.append((nr,nc))
                maze[nr][nc] = 1


# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0 -1, 1]

for tc in range(1, T+1):
    test_case = int(input())
    N = 16
    maze = [list(map(int, input())) for _ in range(N)]
    # print(maze)
    # [
    # [1111111111111111],
    # [1210000000100011],
    # [1010101110101111],
    # [1000100010100011],

    s_c = 0
    s_r = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                s_c = i
                s_r = j
                maze[i][j] = 1


    print(DFS(s_r,s_c))