import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # N = 카드 장수
    N = int(input())
    cards = list(map(int,input()))
    # print(cards)
    # [4, 9, 6, 7, 9]
    # [0, 8, 2, 7, 1]
    # [7, 7, 9, 7, 9, 4, 6, 5, 4, 3]
    counting = [0] * 10
    for i in cards:
        counting[(int(i))] += 1
    # print(counting)
    # [0, 0, 0, 0, 1, 0, 1, 1, 0, 2]
    # [1, 1, 1, 0, 0, 0, 0, 1, 1, 0]
    # [0, 0, 0, 1, 2, 1, 1, 3, 0, 2]
    my_max = counting[0] # 가장 많이 나온 숫자 갯수
    number = 0 # 가장 많이 나온 숫자

    for idx in range(len(counting)):
        # 0 ~ 9
        if counting[idx] == my_max:
            number = idx
        if counting[idx] > my_max:
            my_max = counting[idx]
            number = idx
        # my_max는 가장 많은 장수

    print("#{} {} {} ".format(tc,number,my_max))
