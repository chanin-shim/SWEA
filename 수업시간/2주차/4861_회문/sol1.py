import sys
sys.stdin = open("input.txt")

T = int(input())

# 1) 우선 회문 찾는 식을 구상
# 2) 문장을 나눌수 있는 만큼 다 나눠서 나오게함
# 3) 나온 문장 중에서 M과 길이가 같은 것 선택
# 4) 그 중에서 회문이 돌아가는 거 선택
# 5) 4)까지 통과한 문장이 답

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # print(N, M)
    # # 10 10
    # N은 글자판 크기 N*N
    # M은 회문의 길이여야 하는 것

    result = '이게 나오면 틀렸다는 것임'

    for i in range (1, N+1):
        my_str = str(input())
        # GOFFAKWFSM
        # 01234-5-4-3-2-1 # 인덱스 넘버
        # 이게 회문이 되는 것인지 판별
        for j in range(0, len(my_str)):  # 0 ~ 9
            for k in range(j + 1, len(my_str)):  # 1 ~ 9
                sentence = my_str[j:k]
                # 문장이 나올수 있는 만큼 다 나오게 함
                if len(sentence) == M:
                    if sentence[0:int(M / 2)] == sentence[M-1:int(M / 2):-1]:
                        # 앞에서 절반 출력한거랑, 뒤의 절반을 거꾸로 출력한거랑 같다면
                        result = sentence
                        break

    print("#{} {}".format(tc,result))




    # 못 풀겠다