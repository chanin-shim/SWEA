import sys
sys.stdin = open("input.txt")

T = int(input())


numbers = list(map(int, input().split()))
# print(numbers)
# [85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67, 51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64, 52,] 등등

for i in range(len(numbers)-1,0,-1):
    for j in range(0, i):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
# 버블정렬로 크기순으로 정렬

middle_ond = numbers[round(T/2)-1]
# 어차피 홀수니까 전체에서 가운데 있는걸로 뽑아야함 199개면 100번째껄로
# but 그렇다고 numbers[100]이 아니라, [99]임 왜냐하면 0부터 시작하기 때문에, 99여야 100번째 숫자임.

print("{}".format(middle_ond))

