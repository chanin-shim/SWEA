import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    my_word = str(input())
    # print(my_word)
    # ABCCB

    stack = []
    cnt = 0
    for i in range(len(my_word)):
        stack.append(my_word[i])
        if i < len(my_word)-1:
            if my_word[i] == my_word[i + 1]:
                stack.pop()
    # print(stack)
    # ['A', 'B', 'C', 'C', 'B']



    print("#{} ".format(tc, ))