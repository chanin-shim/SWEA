import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):

    numbers, N = list(map(str,input().split()))
    numbers_list = []
    for i in range(len(numbers)):
        numbers_list += numbers[i]
    # print(numbers_list)
    # ['1', '2', '3']
    # ['2', '7', '3', '7']
    # ['7', '5', '7', '1', '4', '8']
    # ['7', '8', '4', '6', '6']

    numbers_true_list = numbers_list

    len_list = len(numbers_list)
    # 버블솔트
    for i in range(len_list-1, -1, -1):
        for j in range(0, i):
            if int(numbers_list[j]) > int(numbers_list[j+1]):
                numbers_list[j], numbers_list[j+1] = numbers_list[j+1], numbers_list[j]

    # print(numbers_list)
    # ['1', '2', '3']
    # ['2', '3', '7', '7']
    numbers_list = numbers_list[::-1] # 가장 큰 값이 맨 앞으로 오게 뒤집어줌.

    print(int(N))
    temp = ''
    cnt = 0
    for i in range(int(N)):
        temp = numbers_true_list[i]
        numbers_true_list[i] = numbers_list[i] #첫번째 값에 가장큰 값 주기
        for j in range(len_list-1,-1,-1): # 뒤에서 부터 가장 큰 값을 찾아
            if cnt != N:
                if numbers_true_list[j] == numbers_list[i]:
                    numbers_true_list[j] = temp
                    cnt +=1

    # 아 바꿔야 하는 갯수가 많아지면 인덱스번호 넘어가는 걸로 나와서, 이걸 어떻게 해결해야 할 지 모르겠다.




    # print("#{} ".format(tc, ))