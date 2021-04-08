import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1,T+1):
    K, N, M = map(int, input().split())
    my_stations = list(map(int, input().split()))
    # print(K, N, M)
    # print(my_stations)
    # 3 10 5
    # [1, 3, 5, 7, 9]
    # 3 10 5
    # [1, 3, 7, 8, 9]

