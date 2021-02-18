import sys
sys.stdin = open("input.txt")

T = int(input())

# 1) 일단 문자열을 받아옴
# 2) 그리고 긴 문자열을 0~1,0~2,0~3,   0~len(긴문자열)까지 해서 다 나오게해봄
# 3) 그리고 짧은 문자열이 그중 하나라도 들어가는게 있나 물어봄

for tc in range(1, T+1):

    short_str = str(input())
    long_str = str(input())

    # print(str1,str2)
    # XYPV EOGGXYPVSY

    result = 0

    for i in range(0,len(long_str)-1): # 0 ~ 9
        for j in range(i+1,len(long_str)-1): # 1 ~ 9
            if short_str == long_str[i:j]:
                result = 1

    print("#{} {}".format(tc,result))



    # 오답
    # 채점용 input 파일로 채점한 결과 fail 입니다.
    # (오답 : 10개의 테스트케이스 중 6개가 맞았습니다.)

    # 왜지?