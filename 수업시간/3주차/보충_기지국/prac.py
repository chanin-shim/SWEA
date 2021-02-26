arr = [[1,2,3],
 [4,5,6,],
 [7,8,9,]]

        # 12시 방향부터 팔방
     #12 1.5  3 4.5 6, 7.5
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]


r = 1
c = 1

list_8dirc = []
for i in range(8):
    nr = r+dr[i]
    nc = c+dc[i]
    if 0<= nr <3 and 0 <= nc  <3:
        list_8dirc.append(arr[nr][nc])

print(len(list_8dirc))