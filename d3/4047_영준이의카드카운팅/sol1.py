import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):

    card_info = input()
    # print(card_info)
    # S01D02H03H04
    # H02H10S11H02
    # S10D10H10C01

    # each_card_info에 각기 카드 한 장씩의 정보를 담아줌.
    each_card_info = []
    for i in range(0,len(card_info),3):
        each_card_info += [card_info[i:i+3]]

    # print(each_card_info)
    # ['S01', 'D02', 'H03', 'H04']
    # ['H02', 'H10', 'S11', 'H02']
    # ['S10', 'D10', 'H10', 'C01']

    # 각기 카드 문양을 셀 변수 초기화
    cnt_S = 0
    cnt_D = 0
    cnt_H = 0
    cnt_C = 0

    # 각 카드의 첫번째 문양에 맞춰서 cnt+=1씩 해줌
    for i in range(len(each_card_info)):
        if each_card_info[i][0] == 'S':
            cnt_S +=1
        if each_card_info[i][0] == 'D':
            cnt_D +=1
        if each_card_info[i][0] == 'H':
            cnt_H +=1
        if each_card_info[i][0] == 'C':
            cnt_C +=1

    check_set = set()  # 동일한 값이 있나 확인하는 세트
    for i in range(len(each_card_info)):
        check_set.add(each_card_info[i])

    # chect_set에 원소들을 담아서, 겹치는게 있다면, 리스트와 길이가 다를 것이므로
    # 각기 다르게 출력하게 조건을 둠.
    if len(each_card_info) != len(check_set):
        print("#{} {}".format(tc,'ERROR'))
    else:
        print("#{} {} {} {} {}".format(tc, 13 - cnt_S, 13 - cnt_D, 13 - cnt_H, 13 - cnt_C))
