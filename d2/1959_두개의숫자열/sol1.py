import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # print(N,M)
    # 3 5
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))

    long_list = []
    short_list = []

    # 문자열이 먼저받는게 더 클 수도 있으니, short과 long으로 비교
    if len(list_a) >= len(list_b):
        long_list = list_a
        short_list = list_b
    else:
        long_list = list_b
        short_list = list_a

    sum_list = []

    for i in range(len(long_list)-len(short_list)+1): # 0,1
        # i는 큰 리스트 갯수에서 작은 리스트 갯수 뺀 것 만큼 돌 것임 (큰 리스트의 번호를 움직이는 역할)
        tmp = 0
        for j in range(len(short_list)): # 0 ~ 5
            # j는 작은리스트와 큰리스트가 같이 도는 역할을 할거임
            tmp += short_list[j] * long_list[j+i]
            # 작은리스트는 그대로 자기 갯수만큼 돌지만, 큰 리스트는 한 칸 넘어가야 하기 때문에
            # 계산이 다시 시작될 떄마다 i만큼 늘어난 인덱스에서 시작해서, 작은리스트와 같은 갯수로 돌게 설계
        sum_list += [tmp]
        # tmp는 모두 돌때까지의 합을 다 넣고 게산이 끝난후 sum_list에 추가
        # sum_list를 tmp랑 같은 for문에 넣으면 short_list[1] * long_list[1] 계산 할 때마다 들어가서 총 tc=1일때 9개의 경우가 나옴.

    # print(sum_list)
    # [12, -14, 30]
    # [63, 47]
    # [20, -120, -38, 114, -63, -115, 10, -81, -26, 140, -161]

    ans = 0
    for i in sum_list:
        if i > ans:
            ans = i
    # sum_list 중에서 가장 큰값 찾아서 출력

    print("#{} {}".format(tc,ans))