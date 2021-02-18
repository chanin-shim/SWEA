import sys
sys.stdin = open("input.txt")

T = int(input())

# 1) A안에 B가 얼마나 횟수를 체크하고
# 2) 횟수 X len(B)를 구해서
# 3) len(A)에서 그 만큼 뺀다.


for tc in range(1, T+1):
    text_A, text_B = map(str,input().split())
    # print(text_A, text_B)
    # banana bana

    # 1)
    cnt = 0
    for i in range(0,len(text_A)):
        for j in range(i+1,len(text_A)):
            if text_A[i:j] == text_B:
                print(text_A[i:j], text_B)
                cnt += 1
    print(cnt)


    # # 2),3)
    # result = len(text_A) - (cnt * len(text_B)) + cnt

    # print(result)




    print("#{} ".format(tc, ))