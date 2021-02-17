import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    number = int(input())
    #6791400
    # print(number)

    my_list = [2,3,5,7,11]

    # 1) list 하나씩 숫자를 꺼내서
    # 2) number에 나눈다
    # 3) 횟수만큼 cnt+1
    # 4) 몫은 다시 number에 다시 넣어주기
    # 5) 위의 과정을 while문에 넣어서 무한루프
    # 6) 나머지가 0 또는 1이 되면 종료


    # 각기 횟수를 담을 변수 초기화
    cnt_2 = 0
    cnt_3 = 0
    cnt_5 = 0
    cnt_7 = 0
    cnt_11 = 0

    while True:
        for i in my_list:              # [2,3,5,7,11]에서 하나씩 꺼낼거다
            if i == 2:                      # 근데 i ==2라면?
                if number % i == 0:         # 게다가 그 i로 number를 나눌 수 있다면?
                    cnt_2 += 1              # 우선 cnt_2에 1을 더하고 (1회 나눴다는 뜻임)
                    number = number // i    # number에는 그거 나누고 남은 몫을 다시 넣는다.
            elif i == 3:                    # 2가 아니고 3이라면?
                if number % i == 0:
                    cnt_3 += 1
                    number = number // i
            elif i == 5:                    # 5라면?
                if number % i == 0:
                    cnt_5 += 1
                    number = number // i
            elif i == 7:                    # 7이라면?
                if number % i == 0:
                    cnt_7 += 1
                    number = number // i
            elif i == 11:                   # 11이라면?
                if number % i == 0:
                    cnt_11 += 1
                    number = number // i
        if number < 2:      # 혹시 number를 너무 나눠서, 나누는 값 중 가장 작은 2보다 작아지면 멈춰라
            break

    # print(cnt_2,cnt_3,cnt_5,cnt_7,cnt_11)
    # 3 2 2 3 1



    print("#{} {} {} {} {} {}".format(tc, cnt_2, cnt_3, cnt_5, cnt_7, cnt_11 ))


    # 중학교때도 소인수 분해 문제 못풀었던거 같은데, 기분이 좋다.