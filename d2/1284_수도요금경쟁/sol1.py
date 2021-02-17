import sys
sys.stdin = open("input.txt")

T = int(input())



for tc in range(1, T+1):

    P, Q, R, S, W = map(int, input().split())
    # print(P, Q, R, S, W)
    # 9 100 20 3 10

    # P는 A사의 요금
    #################
    # Q는 B사의 기본요금
    # R은 B사의 기준리터
    # S는 기준리터 이상을 사용했을 때 추가 요금
    # (추가임! 최종 요금은 = Q+S)
    # W는 종민이가 쓰는 수도 양

    result = 0
    A_co = P * W # 종민이가 A사에 내는 돈
    B_co = Q # 종민이가 B사에 내는 돈
    B_co_ex = Q + (S * (W-R)) # 종민이가 물을 오바했을 때 B사에 내는 돈

    if W > R:   #만약 종민이가 물을 기준리터보다 과다하게 썼다면
        if A_co > B_co_ex: # A사가 더 비싸다면:
            result = B_co_ex
        else:
            result = A_co

    if W < R:   #만약 종민이가 물을 적게 썼다면
        if A_co > B_co: # P 수도요금이 더 비싸다면?
            result = B_co  # B사를 쓰거라
        else:
            result = A_co


    print("#{} {}".format(tc,result))