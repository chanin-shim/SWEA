import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):

    original_num = input()
    # print(original_num)
    # # 01010101010101010101010101010101010101010101010101
    # # 01
    # # 1000110010011111010110000100100000000001001

    original_int_num = int(original_num)

    original_list = [0] * len(original_num)
    # print(original_list)
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # [0, 0]
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # 몇번째부터 숫자를 바꿔야하는지 인덱스 값 찾기
    number_position =  0
    for i in range(len(original_num)):
        if int(original_num[i]) == 1:
            number_position = i
            break

    # print(number_position)
    # 1
    # 1
    # 0

    for i in range(len(original_list) - number_position):
        if original_list[i] == 1:
            for j in range(i,len(original_list)):
                original_list[j] = 1
            cnt += 1

        # 0이면
        else:
            #first_bit[j] = '0'
            for j in range()




    print("#{} ".format(tc, ))










