import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    print(numbers)
    #[3, 8]

    # 반복문을 돌려서 값을 비교
    for i in range(0,len(numbers)-1) :
        if numbers[i] > numbers[i+1]:
            result = ">"
        elif numbers[i] < numbers[i+1]:
            result = "<"
        else:
            result = "="

    print("#{} {}".format(tc,result))

# 왜 오답으로 나오지?