import sys
sys.stdin = open("input.txt")

T = int(input())

# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

for tc in range(1, T+1):
    N = int(input())
    my_map = [list(map(int,input())) for i in range(N)] # input.split 하면 왜 붙어서 들어오는지 이해가 안감. 오히려 붙이나 안붙이나 떨어져야하는거 아닌가?

    # print(my_map)
    #[
    #[1, 3, 1, 0, 1],
    #[1, 0, 1, 0, 1],
    #[1, 0, 1, 0, 1],
    #[1, 0, 1, 0, 1],
    #[1, 0, 0, 2, 1]
    # ]

    visited = [[0 for _ in range (len(my_map[0]))]for _ in range(len(my_map))]

    # print(visited) # 5x5

    for i in range(N): #visited에 1로 벽 쳐주기
        for j in range(N):
            if my_map[i][j] == 1:
                visited[i][j] = True

    # 시작 지점 찾아주기
    for i in range(N):
        for j in range(N):
            if my_map[i][j] == 2:
                now_r = i
                now_c = j
            if my_map[i][j] == 3:
                end_r = i
                end_c = j

    result = 0
    cnt = 0
    while True:
        for i in range(4):
            nr = now_r + dr[i]
            nc = now_c + dc[i]
            if 0 <= nr < N and 0<= nc < N:
                if (visited[nr][nc] == 0) and (my_map[nr][nc] == 0):
                    visited[nr][nc] = True
                    now_r = nr
                    now_c = nc
                if (visited[nr][nc] == 0) and (my_map[nr][nc] == 3): # 미로 탈출!
                    result = 1


            cnt += 1

        if cnt > 90 or result ==1 :
            break

    print(result)

    # 아마 0을따라 계속 올라가다 3에 갈 수 없으면, 처음지점으로 돌아와서 다른 방향을 둘러봐야하는데
    # 그것이 안되는 것 같음.
