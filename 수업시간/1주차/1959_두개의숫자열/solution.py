def check(long, short):
    for i in range(len(long)-len(short)+1):
        result = 0
        for j in range(len(short)):
            result += long[i+j]*short[j]


T = int(input())


for tc in range(1, T+1):
    # N,M 리스트의 길이를 의미한다. 3~20
    N,M = map(int, input(.split()))

    A = list(map(int,input().split()))
    B= list(map(int, input().split()))

    if N>M:
        ans = check(A,B)
    else:
        ans = check(B,A)

    print



