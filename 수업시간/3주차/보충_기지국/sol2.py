import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1,T+1):
    N = int(input())

    my_town = [list(map(str,input())) for _ in range(N)]

    dr=[-1,1,0,0]
    dc=[0,0,-1,1]

    for i in range(N):
        for j in range(N):
            if my_town[i][j] == 'A':
                r = i
                c = j
                my_list = []
                for k in range(4):
                    nr = r +dr[k]
                    nc = c +dc[k]
                    if 0<=nr<N and 0<=nc<N :
                        if my_town[nr][nc] == 'H':
                            my_town[nr][nc] = 'X'

            if my_town[i][j] == 'B':
                r = i
                c = j
                my_list = []
                for k in range(4):
                    nr = r +dr[k]
                    nc = c +dc[k]
                    if 0<=nr<N and 0<=nc<N :
                        if my_town[nr][nc] == 'H':
                            my_town[nr][nc] = 'X'

    print(my_town)

# [
# ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
# ['X', 'X', 'X', 'H', 'X', 'X', 'X', 'X', 'X'],
# ['X', 'X', 'H', 'A', 'H', 'X', 'X', 'H', 'X'],
# ['X', 'X', 'H', 'H', 'X', 'X', 'X', 'X', 'X'],
# ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
# ['X', 'X', 'A', 'H', 'H', 'X', 'X', 'X', 'X'],
# ['X', 'X', 'H', 'X', 'X', 'H', 'A', 'H', 'X'],
# ['X', 'X', 'A', 'H', 'X', 'X', 'H', 'X', 'X'],
# ['X', 'X', 'H', 'X', 'H', 'X', 'X', 'X', 'X']
# ]