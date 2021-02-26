import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    r = 0
    c = 0

    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    mode = 0

    snail = [[0] * N for _ in range(N)]


    snail[r][c] = 1

    for i in range(2,N**2+1): # 2~16
        if 0<= r + dr[mode] <N and 0<= c + dc[mode] <N and snail[r + dr[mode]][c + dc[mode]]==False :
            nr = r + dr[mode]
            nc = c + dc[mode]

            snail[nr][nc] = i

            r = nr
            c = nc

        else:
            mode +=1
            if mode == 4:
                mode = 0

            nr = r + dr[mode]
            nc = c + dc[mode]

            snail[nr][nc] = i

            r = nr
            c = nc

    print("#{}".format(tc))
    for i in range(N):
        print(*snail[i])


