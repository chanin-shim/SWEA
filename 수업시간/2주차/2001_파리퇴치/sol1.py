import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # 배열은 N * N
    # 파리채는 M * M

    N, M = map(int, input().split())
    # print(N,M)
    # 5 20

    my_matrix = [list(map(int,input().split())) for _ in range(N)]
    # print(my_matrix)
    # [[1, 3, 3, 6, 7], [8, 13, 9, 12, 8], [4, 16, 11, 12, 6], [2, 4, 1, 23, 2], [9, 13, 4, 7, 3]]

    my_max = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sumsum = 0
            for k in range(M):
                for l in range(M):
                    sumsum += my_matrix[i+k][j+l]
                    if my_max < sumsum:
                        my_max = sumsum

    print("#{} {}".format(tc,my_max))