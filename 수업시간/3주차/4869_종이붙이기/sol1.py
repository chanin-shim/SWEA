import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    my_list = [0] * N

    sets = []

    case = 0
    ans = 0

    for i in range(N//10 + 1):
        for j in range(N//10 + 1):
            if 10*i + 20*j == N:
                sets.append([i,j])

    for s in sets:
        if s[1] == 0:
            ans += 1

        # 10,20 둘 다 사용하는 경우

        if s[1]>0 and s[0] >0:
            case += fa(sum(s))//fa(s[0])*fa(s[1])
            # 20을 10의 가로로 나눌 경우
            ans += case * (2**2[1])

