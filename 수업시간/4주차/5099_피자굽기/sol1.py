import sys
sys.stdin = open("input.txt")

T = int(input())

# 처음에 화덕이 꽉차있는건지, 하나씩 넣는건지?

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N = 화덕의 크기
    # M = 피자 개수
    my_cheese = list(map(int, input().split()))

    # print(N,M, '  ', my_cheese)
    # 3 5    [7, 2, 6, 5, 3]
    # 5 10    [5, 9, 3, 9, 9, 2, 5, 8, 7, 1]

    pizza_oven = []

    cnt = 0

    while len(pizza_oven) != N:
        pizza_oven.append(my_cheese.pop(0))

    while True:
        cnt+=1 # 한 사이클을 기록하기 위함
        if len(pizza_oven) != N: # 화덕 최대갯수와 피자수가 안맞는다면
            if len(my_cheese) == 0 : # 피자 갯수가 없다면
                pass
            else:
                while len(pizza_oven) != N: # 계속 채워 넣어주기.
                    pizza_oven.append(my_cheese.pop(0))
        if cnt == N: # 한 바퀴 다 돌았다면
            for i in range(len(pizza_oven)): # 치즈 절반으로 녹음
                pizza_oven[i] = pizza_oven[i]//2
            cnt = 0
        pizza_oven.append(pizza_oven.pop(0)) # 돌리기
        if pizza_oven[0] == 0:
            pizza_oven.pop(0)

        if len(pizza_oven) ==1:
            break


            # 0이면 빼는데, 그럼 어떻게 남은 1개의 인덱스 번호를 알지?
            # 그러면 2차원 리스트로 해서, 나가도 자리를 남겨놔야 하나?










    print("#{} ".format(tc, ))