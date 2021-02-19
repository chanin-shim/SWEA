import sys
sys.stdin = open("input.txt")

T = int(input())

# 1) 단어 거꾸로 돌리는 함수 만들기
# 2) 단어 input 받기
# 3) 단어 == reverse(단어) 입니까? 맞으면 1, 아니면 0

# 1)
def word_reverse(word):
    reverse_word = ''
    for i in range(len(word)-1,-1,-1):
        reverse_word += word[i]
    return reverse_word



for tc in range(1, T+1):

    # 2)
    my_word = input()
    ans = 0

    # 3)
    if word_reverse(my_word) == my_word:
        ans = 1
    else:
        ans = 0

    print("#{} {}".format(tc,ans))




    # 사담
    # 아 다른분들의 풀이를 보니
    # str[::-1]하면 쉽게
    # 거꾸리가 나온다.