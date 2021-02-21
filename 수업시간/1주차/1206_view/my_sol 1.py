import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    caet_len = int(input())
    # print(caet_len)
    # 100
    case_list = list(map(int, input().split()))
    # print(case_list)
    #[0, 0, 225, 214, 82, 73, 241, 233, 179, 219, 135, 62, 36, 13, 6, 71, 179, 77, 67, 139, 31, 90, 9, 37, 93, 203, 150, 69, 19, 137, 28,
    # n-2 n-1 n n+1 n+2 해서
    # n과 나머지4개중 최대값을 뺴면 되는 문제
    ans = 0
    for i in range(2, len(case_list)-2):
        max_num = 0
        max_looking_list = []
        for j in range(-2,3):
            if j == 0: # 0나오면 자기자신이니까 빼줬음
                continue
            else:
                if case_list[i-j] > max_num:
                    max_num = case_list[i-j]

        # 조망권 확보라는 개념. 적어도 자기가 자기다음으로 큰 빌딩보다는 커야함
        if case_list[i] > max_num:
            ans += case_list[i] - max_num

    print("#{} {}".format(tc,ans))





