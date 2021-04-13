import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = input().split()
    N = int(N)
    M = int(M)

    arr = []
    while M>0:
        arr.append(M%2)
        M = M//2
    arr= arr[::-1] # 거꾸로 출력되길래, 보기 좋게 뒤집음
    # print(arr)
    # [1, 1, 1, 1, 0]
    # [1, 0, 1, 1, 1, 1]
    # [1, 1, 1, 1, 1]
    # [1, 1, 1, 1, 1, 0]

    result = 'ON'  # 별일 없다면 ON 출력

    last = len(arr) - 1
    for i in range(last, last - N, -1):  # 끝 값 ~ 끝 -N 값까지 차례로 나와라 (인덱스로 쓰게)
        if len(arr) < N:  # 아예 기준미달, N개를 확인조차 못하는 애들은 거르기.
            result = 'OFF'

        else:  # 적어도 N개는 넘는다면
            if arr[i] == 0:  # 끝값에서 부터 N개까지 하나씩 검사를 해서 0이 하나라도 나온다면
                result = 'OFF'  # 결과는 OFF

    print("#{} {}".format(tc, result))
