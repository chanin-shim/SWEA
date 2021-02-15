import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # N : 정수의 총 갯수
    # M : 구간의 갯수
    N,M = map(int,input().split())
    # print(N, M)
    # (10 3)
    inp_arr = list(map(int,input().split()))
    # print(inp_arr)
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # [6262, 6004, 1801, 7660, 7919, 1280, 525, 9798, 5134, 1821]
    # [3266, 9419, 3087, 9001, 9321, 1341, 7379, 6236, 5795, 8910, 2990, 2152, 2249, 4059, 1394, 6871, 4911, 3648, 1969,
    #  2176]

    min_ = 10000 * M # 정쉬 최대값 * 구간길이
    max_ = 0

    for i in range(N-M+1) :
        tmp = 0
        for j in range(M):
            tmp += inp_arr[i+j]

        print(tmp)


    # print("#{} ".format(tc, ))

