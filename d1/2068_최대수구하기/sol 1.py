import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1,T+1):
    numbers = list(map(int, input().split()))
    # print(numbers)
    # [3, 17, 1, 39, 8, 41, 2, 32, 99, 2]
    max_number = 0
    for i in numbers:
        if max_number < i:
            max_number = i

    print("#{} {}".format(tc, max_number))