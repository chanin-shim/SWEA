import sys
sys.stdin = open("input.txt")

T = int(input())

    # 1) 버블 정렬로 정렬 후
    # 2) numbers_list[i+1], numbers_list[j-1]씩 출력하기

for tc in range(1, T+1):
    number = int(input())
    numbers_list = list(map(int,input().split()))
    # print(number, numbers_list)
    # 10 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for i in range (len(numbers_list)-1,0,-1):
        for j in range(0,i): # 0 ~9, 0~8, 0~7
            if numbers_list[j] > numbers_list[j+1]:
                numbers_list[j], numbers_list[j+1] = numbers_list[j+1], numbers_list[j]
    # 버블정렬로 예쁘게 정렬

    # print(numbers_list)
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #  0  1  2  3  4  5 -4  -3  -2 -1 (인덱스가 이렇게 됨)



    print('#{}'.format(tc,), end=" ")
    for i in range(1,6):
        print(numbers_list[-i], numbers_list[i-1],end=" ")
    print('')