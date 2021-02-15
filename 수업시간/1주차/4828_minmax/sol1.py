import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    max_result = numbers[0]
    min_result = numbers[0]
    for i in numbers:
        if i >= max_result:
            max_result = i

    for j in numbers:
        if j <= min_result:
            min_result = j

    final = max_result - min_result
    print("#{} {}".format(tc,final))
#
#
# import sys
# sys.stdin = open("input.txt")
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     numbers = list(map(int, input().split()))
#     max = numbers[0]
#     min = numbers[0]
#     for i in range(0, N):
#         if numbers[i] > max:
#             max = numbers[i]
#         elif numbers[i] < min:
#             min = numbers[i]
#         else:
#             continue
#     result = max - min
#     print("#{} {}".format(tc, result))