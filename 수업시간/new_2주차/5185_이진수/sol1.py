import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N, words = input().split()
    N = int(N)
    final_list = []
    for i in range(N):
        my_list = []
        cnt = 0  # 횟수 초기화
        if words[i] not in 'ABCDEF' :
            num = int(words[i])
            while num > 0:
                my_list += [num % 2]
                num = num // 2
                cnt += 1
            if cnt < 4:  # 2진수 4자리를 다 못채웠을 시
                rest = 4 - cnt
                for j in range(rest):  # 못채운 자리수 만큼
                    my_list += [0]  # 0을 더해줌.
            final_list += my_list[::-1]
        else:
            if words[i] == 'A':
                num = 10
            if words[i] == 'B':
                num = 11
            if words[i] == 'C':
                num = 12
            if words[i] == 'D':
                num = 13
            if words[i] == 'E':
                num = 14
            if words[i] == 'F':
                num = 15
            while num > 0:
                my_list += [num % 2]
                num = num // 2
            final_list += my_list[::-1]

    # print(final_list)
    result = ''
    for i in final_list:
        result += str(i)
    print("#{} {}".format(tc,result))