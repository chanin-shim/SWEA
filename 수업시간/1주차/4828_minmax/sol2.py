import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    # print(numbers)
    # [477162, 658880, 751280, 927930, 297191]

    # 가장 큰 수, 작은 수 빼기 !


    # 오랜만에 킹블솔트
    for i in range(len(numbers)-1,-1,-1):
        for j in range(0,i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    # print(numbers)
    # [297191, 477162, 658880, 751280, 927930]

    print("#{} {}".format(tc,numbers[len(numbers)-1] - numbers[0]))