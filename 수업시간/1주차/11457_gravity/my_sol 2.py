import sys
sys.stdin = open("input.txt")

T = int(input())

# 길이가 가장 긴것이 아니라,
# 차이가 가장 큰것을 골라야함.
# 그 차이, 낙차를 구하면 됨.

# [0] 이중 포문에 넣어서 이차원 배열로 풀어도 가능할듯.

for tc in range(1, T+1):
    N = int(input()) # 방의 길이
    case_numbers = list(map(int, input().split())) #주어지는 숫자열 리스트
    # [7 4 2 0 0 6 0 7 0]

    my_list = [[0 for _ in range(N)]for _ in range(N)]
    # print(my_list)
    # 잘 만들어짐

    for i in range(N): # 0~ 8
        for j in range(case_numbers[i]):
            my_list[::-1][j][i] += 1




    print("#{} ".format(tc, ))