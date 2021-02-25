import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):

    N, M, K = map(int,input().split())
    # print(N, M, K)
    # 74 60 97
    # N = 사람 수
    # M = M초의 시간
    # K = 붕어빵 수

    coming_time = list(map(int, input().split()))
    # print(coming_time)
    # [59, 60, 60, 61, 60, 60, 61, 59, 60, 61, 60, 59, 59, 59, 60, 61, 61, 60, 60, 59, 60, 61, 59, 61,



