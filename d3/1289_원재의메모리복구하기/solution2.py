import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    digit_list = list(map(int,input()))
    N = len(digit_list)
    my_list = [0]*N

    cnt = 0

    for i in range(N):
        if my_list[i] == digit_list[i]:
            pass
        elif my_list[i] != digit_list[i]:
            cnt += 1
            for j in range(N-i):
                my_list[j+i] = digit_list[i]

    print("#{} {}".format(tc, cnt))
