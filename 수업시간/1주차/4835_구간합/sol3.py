import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N,M = map(int, input().split())
    numbers = list(map(int,input().split()))
    # print(N,M)
    # print(numbers)
    # 10 3
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    max_case = 0
    min_case = 10000 * 100
    for i in range(0,N-M+1):
        sumsum = 0
        for j in (numbers[i:i+M]):
            sumsum += j
        if sumsum > max_case:
                max_case = sumsum
        if sumsum < min_case:
                min_case = sumsum

    print(max_case - min_case)
