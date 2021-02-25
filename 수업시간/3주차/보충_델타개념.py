# 내가 있는 위치를 기준으로 사방이든 팔방이든 확인해보고,


dr = [] # row
dc = [] # column

# 상, 하 , 좌, 우
dr = [-1 1 0 0]
dc = [0 0 -1 1]


arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

r = 1
c = 2  # 이게 6

# r = 1
# c = 0 # 이게 4

for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]

    # if 0<=nr <3 and 0 <=nc <3:
    #     print(arr[nr][nc])

    # if nr < 0 or nr >= 3 or nc < 0 or nc >= 3:
      #  continue
    #   print(arr[nr][nc])
    # 위와 같음.

# ** - 값은 뒤로가고, +로 늘어나면 인덱스 에러가 남.


# 한 칸씩 이동할 때 말고 여러칸 이동할 때는 r,c들을 += 로 갱신하면서 나아가면 됨!

팔방
dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]

nr = r #new row로 새로 저장해줌.
nc = c


nr += dr[i] # 일단 이동 하는 거임
nc += dc[i]




# break를 쓰면 가장 가까이 있는 반복문이 짤려버림.