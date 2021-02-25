import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    numbers = input()
    sell_price = list(map(int,input().split()))
    # print(sell_price)
    #     [522, 4575]
    # [6426, 9445, 8772, 81, 3447]

    max_price = sell_price[::]
    for i in range(len(max_price)-1,-1,-1):
        for j in range(0,i):
            if max_price[j] > max_price[j+1]:
                max_price[j], max_price[j+1] = max_price[j+1] , max_price[j]
    reverse_max_price = max_price[::-1]
    # print(reverse_max_price)
    # [4575, 522]
    # [9445, 8772, 6426, 3447, 81]

    sumsum = 0
    for i in reverse_max_price: # [10 7 6]
        for idx in range(len(sell_price)): #0 1 2
            if sell_price[idx] == i:
                for j in sell_price[sell_price.index(i)+1:idx+1]:
                    sumsum += i-j

    print(sumsum)

    # 맥스값찾고 그 가장 큰값 전까지 는 다 사서, 맥스값에 팔아줌
    # 그 다음 맥스값을 찾고
    # [원래 맥스값 팔았던 곳에서 부터 시작 : 그다음 맥스값]까지 다 사서 팔아줌. 반복

