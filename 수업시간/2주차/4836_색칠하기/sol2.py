import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1,T+1):
    try_num = int(input())

    total = [[0 for _ in range(10)] for _ in range(10)]

    for i in range (try_num):
        x1, y1, x2, y2, color = map(int, input().split())
        # x축의 값은 2차원 리스트 안에서
        # y축의 값은 큰 리스트 안에서
        for i in range(x1, x2+1): #2,3,4
            for j in range(y1, y2+1): #3,4,5,6
                total[i][j] += color

    cnt = 0
    for i in total:
        for j in range(len(total)):
            if i[j] >= 3:
                cnt +=1

    print(cnt)

