import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    my_list = []

    # ABCDE 처럼 붙어있는 글자를
    # ['A','B','C']이런식으로 각기 리스트에 넣을 수 있는가

    # error가 뜬다면 이렇게 해라 라고 if문으로 지시하고싶은데
    # 그건 어떻게 해야하는건지 if aa == error 이렇게 하는건 아닌거같다.



    print("#{} ".format(tc, ))