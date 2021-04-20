import sys
sys.stdin = open("input.txt")

T = int(input())

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# y,x,카운트, 지금까지 적립해온 문자열
def solve(y,x,c,s):
    # 이동이 6번이면 set에 추가
    if c == 6:
        r.add(s)
        return
    # 4방향 탐색
    for d in range(4):
        ty, tx = y+dy[d], x+dx[d]
        # 범위를 넘어가는지 확인
        if 0<=ty<4 and 0<=tx<4:
            solve(ty, tx, c+1, s+grid[ty][tx])

for tc in range(1, T+1):
    grid = [list(input().split())for i in range(4)]
    r = set()
    # 16개의 시작점 모두를 탐색한다.
    for i in range(4):
        for j in range(4):
            solve(i, j, 0, grid[i][j])
    print("#{} {}".format(tc, len(r)))

