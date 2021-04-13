import sys
sys.stdin = open("input.txt")

T = int(input())

# set은 중복이 없으니까, 모든 경우를 set에 넣고 그 len을 구하자

for tc in range(1, T+1):
    N = int(input())
    point_list = list(map(int,input().split()))
    # print(point_list)
    my_set = set()

    # 일단 개별로 더하기
    for i in range(N):
        my_set.add(point_list[i])

    print(my_set)






    print("#{} ".format(tc, ))