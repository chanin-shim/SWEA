import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    number = int(input())


    odd_sum = 0
    even_sum = 0
    for i in  range(1, number+1): # 1부터 받은 숫자값 까지의 길이설정
        if i % 2 == 1: # 홀수일 때
            odd_sum += i
        elif i % 2 == 0:
            even_sum += i

    result = odd_sum - even_sum

    print("#{} {}".format(tc, result))