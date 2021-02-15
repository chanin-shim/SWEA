import sys
sys.stdin = open("input.txt")

T = 10


for tc in range(1, T+1):
    building_count = int(nput())
    building_list = list(map(int, input().split()))

    # 조망권이 확보된 집
    total = 0

    for i in range(building_count):
        now = building_list[i]
        # now = 현재위치
        if now == 0:
            continue
        else:
            # 최대 높이 저장용
            max_height = 0
            for j in range(4):
                idx = [-2,-1,1,2]
                building_list[i - 2]

                if building_list[i+idx[j]] > max_height:
                    max_height = building_list[i+idx[j]]

            # 내가 나머지 네개보다 크다면
            if now > max_height:
                total += now - max_height

                if building_list[i+idx[j]]:

    print("#{} ".format(tc, ))

