import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1,T+1):
    num = int(input())
    card = str(input())
    # print(num, card)
    # 5 49679

    my_list = [0 for _ in range(10)]

    for i in range(len(card)):
        my_list[int(card[i])] += 1

    # print(my_list)
    # [0, 0, 0, 0, 1, 0, 1, 1, 0, 2]
    max_num = my_list[0]
    card_num = 0
    for i in range(len(my_list)):
        if max_num <= my_list[i]:
            max_num = my_list[i]
            card_num = i


    print("#{} {} {}".format(tc,card_num, max_num))