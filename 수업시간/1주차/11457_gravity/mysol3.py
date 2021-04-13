# import sys
# sys.stdin = open('input.txt')
#
# T = int(input())
#
# for tc in range(1,T+1):
#     N = int(input())
#
#
#
#

arr = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,16],
       ]

r = 1
c = 1
N = 4
# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

drc = [[-1,0], [1,0],[0,-1],[0,1]]

for i in range(4):
    nr = r+dr[i]   #nr = next_r, r = 현재 내가있는 r
    nc = c+dc[i]

    # if nr <0 or nr >= N or nc < 0 or nc >=N


#전치행렬
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if i > j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

print(arr)
