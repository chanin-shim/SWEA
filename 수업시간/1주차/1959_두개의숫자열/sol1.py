import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N, M = map(int,input().split())
    # N = list_short 숫자 갯수
    # M = list_long 숫자갯수
    list_short = list(map(int,input().split()))
    list_long = list(map(int,input().split()))

    #일단 리스트short을 리스트 long의 [0,1,2] [1,2,3] [2,3,4] 다 더하게 한다.
    #그리고 그 각기 더한 값들을 비교해서 최고값을 구한다.
    total = 0
    number = 0
    result = []
    temp = []
    temp_num = 0
    # list_short가 더 많을수도 있으니까 두개를 바꿔줌.
    # 반드시 이름에 맞춰서 짧은게 short으로 가게
    if len(list_short) > len(list_long):
        temp = list_short[:]
        list_short = list_long[:]
        list_long = temp[:]
    # 각기 숫자도 바꿔줌
        N = temp_num
        N = M
        M = temp_num

    while True:
        for i in range(N):
            total += list_short[i] * list_long[i+number]
        result += [total]
        # 더한 값을 result에 저장해줌
        number += 1
        # number를 하나올려서 list_long이 한칸씩 더가서 계산되게 함.
        if number >= M-N+1:
            break
    max_result = result[0]
    for i in result:
        if max_result < i:
            max_result = i

    print("#{} {}".format(tc,max_result))

