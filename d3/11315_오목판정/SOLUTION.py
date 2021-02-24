import sys
sys.stdin = open("input.txt")

# 오른쪽 = 행:그대로, 열:+1/ 오른아래 행:+1, 열:+1 / 아래 행:+1, 열:0 / 왼아래 행:+1, 열:-1
dr = [0,1,1,1]
dc = [1,1,0,-1]

def chech():
    #이차원을 순회 하면서 해당 정점을 시작으로 4군데 검사를 시작한다.
    for i in range(N):
        for j in range(N):
            # 4방향을 살펴 볼 것
            for k in range(4):
                o_cnt = 0
                nr, nc = i,j

                # 순서가 바뀌면 매우 곤란함.
                while 0<=nr<N and 0 <=nc<N and arr[nr][nc] == 'o':
                    o_cnt +=1
                    if o_cnt == 5:
                        return 'YES'
                    nr += dr[k]
                    nr += dc[k]


T = int(input())

for tc in (1,T+1):
    N = int(input())

    # 오목판 입력
    arr = [input() for _ in range(N)]


