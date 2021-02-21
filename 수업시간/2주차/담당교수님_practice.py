# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# for i in range(len(a)):
#     for j in range(len(a[0])):
#         print (a[i][j]) (가로)
#         print (a[i][j]) (세로)
#
# 십진수 세상에서 뒤에 0을 붙인다는건 * 10을 해준다는 것
# 이진수 세상에서 뒤에 0을 붙인다는건 * 2를 해준다는
#
# 컴퓨터는 연산보다 계산이 훨씬 빠르다
# 89 * 100은 사실상 89를 100번 더하는 것
# -> 그것보다  89<<2 두칸 옆으로 가
# -> 이게 훨씬 빠른 것





#----
arr = [[1,2,3,4,],[5,6,7,8,],[9,10,11,12]]

# 행 정렬 할거면 행길이먼저 (for i in range(len(arr)))
# 열 정렬 할거면 열길이먼저 (for i in range(len(arr[0]))
# 행 역순, 열 역순, 행을 역순한 열의 역순 다 자유롭게 연습하기.

# 지그재그 순회
for i in range(len(arr)):
    if i % 2 == 1:
       for j in range(len(arr[0])-1,-1,-1):
           print(arr[i][j])
    else:
        for j in range(len(arr[0])):
            print(arr[i][j])



