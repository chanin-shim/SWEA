import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    N = int(input())
    words = list(input())
    # print(words)
    # ['(', '(', '{', '<', '(', '(', '{', '{', '[', '[', '[', '[', '<', '<', '[', '[', '(', '<', '[', '[', '{', '(', '[',
    #  '{', '{', '{',

    stack = []
    result = 1
    for i in range(len(words)):
        a = words[i]
        if words[i] == "{" or words[i] == "(" or words[i] == "[" or words[i] == "<":
            stack.append(words[i])

        # 닫는 괄호
        else:
            # 없는데 들어오면 break
            if not len(stack):
                result = 0
                break
            # 있긴 있다
            else:
                # 짝이 맞는 경우면 pop
                if stack[-1] == '(' and words[i] == ')' or stack[-1] == '[' and words[i] == ']' or stack[-1] == '{' and words[i] == '}' or stack[-1] == '<' and words[i] == '>':
                    stack.pop()
                else:
                    #짝이 안맞으면 break
                    result=0
                    break
    else:
        if len(stack):
            result = 0

    print("#{} {}".format(tc, result))
