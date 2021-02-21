import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1,T+1):
    N = int(input())

    my_list = [[0 for _ in range(10)] for _ in range(10)]

    for i in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
        for x in range (x1,x2+1):
            for y in range (y1,y2+1):
                my_list[y][x] += 1

    cnt = 0
    for i in range(len(my_list)):
        for j in range(len(my_list[0])):
           if my_list[i][j] == 2 :
               cnt+=1
    print(cnt)