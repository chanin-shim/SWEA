import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1,T+1):
    num = int(input())
    card = input()

    # print(card)
    # 49679
    # 08271
    # 7797946543

    check_list = [0] * 10


    for i in range(len(card)):
        check_list[int(card[i])] += 1

    max_num = check_list[0]
    num = 0
    cnt = 0
    for i in check_list:
        cnt += 1 # 인덱스 번호가 실제 숫자 값이므로, 인덱스 값과 같이 하나씩 늘려줘서, 실제 숫자와 같게 해줌
        if i >= max_num:
            max_num = i
            num = cnt -1
    print(check_list)

    print("#{} {} {}".format(tc,num,max_num))
