import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):

    N = int(input())

    my_list = []
    for _ in range(N):
        my_list.append(list(map(int,input().split())))
    # print(my_list)
    # [
    # [1, 2, 3],
    # [4, 5, 6],
    # [7, 8, 9]
    # ]



    # 너무 어려워 모르겠다.
    # 규칙성 자체가 이해가 안감.





    print("#{} ".format(tc, ))