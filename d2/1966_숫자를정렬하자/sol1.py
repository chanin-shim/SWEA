import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    text_num = int(input())
    text_list = list(map(int,input().split()))

    #버블솔트로 시원하게 정렬
    for i in range(len(text_list)-1,-1,-1):
        for j in range(0,i):
            if text_list[j] > text_list[j+1]:
                text_list[j] , text_list[j+1] = text_list[j+1] , text_list[j]



    print("#{}".format(tc),end=" ")
    for i in text_list:
        print(i,end=" ")
    print("")