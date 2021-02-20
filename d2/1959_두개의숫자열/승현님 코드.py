import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split())) # N, M = list(map(int, input().split()))과
                                     # N, M = map(int, input().split())의 출력 결과가 같은데 이유가 뭘까?

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    print(A,B)



    #함수는 결국 하나의 값만 리턴
    # def ~~~ return 1,2이고
    # a = (1,2)로 나옴.

    # N = list(map()) # N = list
    # a, b = N #