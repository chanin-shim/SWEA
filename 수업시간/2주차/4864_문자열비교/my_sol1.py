import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # N 은 문자열 길이
    # M 은 문자열2 길이
    str_1 = str(input())
    str_2 = str(input())
    # print(str_1, str_2)
    # XYPV EOGGXYPVSY

    ans = 0
    for i in range(len(str_2)):
        for j in range(i,len(str_2)+1):
            if str_2[i:j] == str_1:
                ans += 1

    print("#{} {}".format(tc,ans))