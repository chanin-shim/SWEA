arr = [[1,2,3,4],
       [5,6,7,8],
       [10,11,12,13]
       ]

N = 3 #행의 길이 len(arr)
M = 4 #열의 길이 len(arr[0])

#행 우선순회 방식
for i in range(N):
    for j in range(M):
        print(arr[i][j])

#행 우선순회를 역으로 돌아보자!
for i in range(N):
    for j in range(M-1,-1,-1):
        print(arr[i][j])

#열 우선순회 방식 #j의 값은 고정돼있고, i의 값이 변화면서 가져온다.
for j in range(len(arr[0])):
    for i in range(len(arr)):
        print(arr[i][j])

#열 우선순회를 역으로 돌아보자
for j in range(M):
    for i in range(N-1,-1,-1):
        print(arr[i][j])

# 지그재그 순회
for i in range(len(arr)):
    for j in range(len(arr[0])):
        arr[i][j + (m-1-2*j) * (i % 2)]
        #위에 거 말고 그냥 i문다음에 if하고 그 안에서 for로 j돌리는게 나음.


########################################################################################################################














