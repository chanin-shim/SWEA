import sys
sys.stdin = open("input.txt")

T = 10

#상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def BFS(r,c):
    Q = [(r,c)]

    while Q:
        cur_r , cur_c = Q.pop(0)
        # 서있는 위치가 도착지점인가?
        for i in range(4):
            nr = cur_c+dr[i]
            nc = cur_c+dr[i]

            if nr< 0 or nr>N or nc<0 or nc>-N:
                continue

            if maze[nr][nc] == 3:
                return 1

            #갈 수 있는 자리라면
            if maze[nr][nr] != 1:
                Q.append((nr,nc))
                maze[nr][nc] = 1 # 방문 체크


for tc in range(1, T+1):
    N = 16
    test_num = int(input())
    maze = [list(map(int,input()))for _ in range(N)]


    for i in range (N):
        for j in range(N):
            if maze[i][j] == 2:
                sR = i
                sC = j
                maze[i][j] = 1

    print(BFS(sR,sC))