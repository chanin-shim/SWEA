import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
# K = 한번 충전으로 이동할수있는 수
# N = 종점
# M = 충전기가 설치된 정류장 수
    K,N,M = map(int,input().split())
    #(3,10,5)
    station_sum = list(map(int,input().split()))
    #[1, 3, 5, 7, 9]
    # 1) 일단 간다
    current = 0
    charge = 0
    while True :
        current += 3
        if current >= N:
            break
        else:
            while True:
                if current in station_sum:
                    charge += 1

                else:
                    for i in station_sum:
                        current






    print("#{} {}".format(tc, ))

