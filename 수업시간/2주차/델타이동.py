# 델타를 이용한 2차 배열 검색

arr = [[1,2,3],
       [4,5,6],
       [7,8,9]
       ]

r = 1
c = 1
N = 3

#상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]
#상하좌우
drc = [[-1,0],[1,0],[0,-1],[0,1]]

for i in range(4):
    nr = r+dr[i]
    nc = c+dc[i]

    if nr < 0 or nr >= N or nc < 0 or nc >=N: continue
    print(arr[nr][nc])
    # 이 범위를 넘어서면 하지마 !

    if 0 <= nr < N and 0 <= nc < N:
        print(arr[nr][nc])
    # 이거는 이 범위 안에서만 해!


