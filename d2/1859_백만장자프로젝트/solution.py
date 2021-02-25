import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))
    result = 0

    # 일단 최대값 찾자
    max_price = 0
    max_idx = 0
    for i in range(N):
        if price[i] > max_price:
            max_price = price[i]
            max_idx = i
    # 가장 큰 가격의 앞 자료들은 모두 이익이다!
    for i in range(max_idx):
        result += (max_price - price[i])

    max_price = 0
    # 나머지 처리하기 / 뒤에서부터 읽자
    for i in range(N - 1, max_idx + 1, -1):
        if price[i] > max_price:
            max_price = price[i]
        if price[i - 1] < max_price:
            result += max_price - price[i - 1]

    print("#{} {}".format(tc, result))