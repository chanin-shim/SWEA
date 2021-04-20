import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    my_word = str(input())
    stack = []

    for i in range(len(my_word)):
        if len(stack) ==0: # 하나도 없으면 일단 ㅓㄶ기
            stack.append(my_word[i])
        elif stack[-1] == my_word[i]: # 스택에 가장 최근에 들어간게, 지금 하나 뽑힌 글자랑 같다면,
            stack.pop() # 바로 스택에서 아웃 (새로 뽑힌 한글자는 아예 append를 안해주니까 따로 pop할필요가 없음)
        else:
            stack.append(my_word[i]) # 위와같은 상황이 아닐시 스택에 저장해주기.

    print("#{} {}".format(tc,len(stack)))

