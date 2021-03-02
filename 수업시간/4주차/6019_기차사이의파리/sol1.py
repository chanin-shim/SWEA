import sys
sys.stdin = open("s_input.txt")

T = int(input())


for tc in range(1, T+1):

    D,A,B,F = map(int, input().split())
    # print(D,A,B,F)
    # 250 10 15 20
    # D = Distance
    # A, B = A,B기차의 속력
    # F = 파리의 속력

    C = A+B
    # 시간당 가까워 지는 정도

    N = D/C

    fly_distance = 0
    distance_A = 0
    distance_B = 0
    fly_position = 0

    toword = 'to B'

    while True:
        if toword == 'to B':
            distance_A += A
            distance_B += B
            fly_distance += F
            fly_position += F
            if B == D-F:
                fly_position = 0
                toword = 'to A'
            D -= C
        if toword == 'to A':
            distance_A += A
            distance_B += B
            fly_distance += F
            if A == D-F:
                fly_position = 0
                toword = 'to B'
            D -= C

        if D == 0:
            break

    print("#{} {}".format(tc,fly_distance))