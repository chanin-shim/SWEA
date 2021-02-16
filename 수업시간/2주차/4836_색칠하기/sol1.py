import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    # 2
    red_list = []
    blue_list = []
    # red값과, blue값을 담을 리스트 생성

    for i in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if color == 1:
                    red_list.append((x,y))
                elif color == 2:
                    blue_list.append((x,y))
    # print(red_list, blue_list)
    # [(2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (3, 4), (4, 2), (4, 3), (4, 4)] = red_list
    # [(3, 3), (3, 4), (3, 5), (3, 6), (4, 3), (4, 4), (4, 5), (4, 6), (5, 3), (5, 4), (5, 5), (5, 6), (6, 3), (6, 4), (6, 5), (6, 6)] = blue_list

    cnt = 0
    for i in range(len(red_list)):
        if red_list[i] in blue_list:
            print(red_list[i])
            cnt +=1

    print("#{} {}".format(tc, cnt))
