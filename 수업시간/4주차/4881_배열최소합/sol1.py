import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    my_list = []
    for _ in range(N):
        my_list.append(list(map(int,input().split())))

    # print(my_list)
    # [
    # [2, 1, 2],
    # [5, 8, 5],
    # [7, 2, 2]
    # ]

    temp= []
    for i in range(N): # 행

        for j in range(N): #열
            my_list[i][j]
    print(temp)




    print("#{} ".format(tc, ))