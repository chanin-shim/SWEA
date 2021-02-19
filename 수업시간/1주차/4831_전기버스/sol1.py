import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
# K = 한번 충전으로 이동할수있는 수
# N = 종점
# M = 충전기가 설치된 정류장 수
    K,N,M = map(int, input().split())
#     print(K,N,M)
#     3 10 5
    station_list = list(map(int,input().split()))
    # print(station_list)
    # [1, 3, 5, 7, 9]

    my_position = 0
    cnt = -1
    while True:
        my_position += K # k만큼 전진해라.
        cnt += 1
        if my_position in station_list:
            my_position += 0 # K만큼 전진한게 station_list에 있다면 괜찮아.
        else: # 근데 아니라면
            for i in range(1, len(station_list)): # 1~4
                if station_list[i - 1] < my_position < station_list[i]:
                    my_position = station_list[i - 1] # 충전기있었던 뒤로 물러나
                    if my_position + K < station_list[i]: #근데 물러난상태에서 최대값만큼 가려고해봤자 다음 값에 도달못한다면
                        cnt = -999 #횟수 -999로 만들고 for문 밖으로 나가
                        break
        if my_position >= N:
            break
        if cnt == -999:
            cnt = 0
            # 자 여기서 왜 굳이 -999로 하고 다시 0으로 만들어 줬느냐
            # while 문 안의 for문 안의 if문에서 break써봤자 못빠져나오길래, 그냥 일로 데려와서 다시 cnt=0으로 하고 끝내버렸다.
            # 어떻게 짧고 명료하게 빠져나갈 수 있을까?
            break

    print("#{} {}".format(tc,cnt))

