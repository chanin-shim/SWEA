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
    # print(case_num, case_numbers)
    # 9
    # [7, 4, 2, 0, 0, 6, 0, 7]

   # 일단 길이 최고값은 찾아야해
    max_num = 0
    max_index = 0
    for i in range(N):
        if max_num < case_numbers[i]:
            max_num = case_numbers[i]
            max_index = i

        for i in range(N): # 전부 가장 긴 값의 인덱스 값에서
            if i >= max_num


                # 만약 전부 맨밑으로 떨어지는게 그게 더 크다면 그게 final_max값이 돼라





    print("#{} ".format(tc, ))