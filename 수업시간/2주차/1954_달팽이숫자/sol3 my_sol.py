import sys
sys.stdin = open("input.txt")

T = int(input())

# 시계방향
dr = [0,1,0,-1]
dc = [1,0,-1,0]

for tc in range(1, T + 1):
    N = int(input())

    # N*N 리스트 만들기
    snail = [[0] * N for _ in range(N)]

