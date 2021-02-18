import sys
sys.stdin = open("input.txt")

T = int(input())





for tc in range(1, T+1):

    str_1 = str(input())
    str_2 = str(input())

    # print(str_1,str_2)
    # XYPV EOGGXYPVSY


    max_num = 0
    for i in str_1:
        sum_num = 0
        for j in str_2:
            if i == j:
               sum_num += 1
            if sum_num >= max_num:
                max_num = sum_num

    print("#{} {}".format(tc,max_num))