import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    my_farm = [list(map(int,input()))for _ in range(N)]
    # print(my_farm)
    # [[1, 4, 0, 5, 4], [4, 4, 2, 5, 0], [0, 2, 0, 3, 2], [5, 1, 2, 0, 4], [5, 2, 2, 1, 2]]

    middle = N//2

    farm_sum = 0
    for i in range(N): #0 ~4
        if i <= middle:
            for j in my_farm[i][middle-i:middle+i+1]:
                farm_sum += j
        else: # 3,4
            for j in my_farm[i][middle-(N-1-i):middle+(N-1-i)+1]:
                farm_sum += j

    print("#{} {}".format(tc,farm_sum))