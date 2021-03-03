import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())

    distance = 0
    velocity = 0
    for i in range(N):
        my_list = list(map(int, input().split()))
        if my_list[0] == 1: # 가속일때
            velocity += my_list[1]
            distance += velocity
        if my_list[0] == 2: # 감속일때
            if velocity - my_list[1] <0: #감속할 속도가 더 크다면:
                velocity == 0
            else:
                velocity -= my_list[1]
                distance += velocity
        if my_list[0] == 0:
            distance += velocity

    print("#{} {}".format(tc,distance))
