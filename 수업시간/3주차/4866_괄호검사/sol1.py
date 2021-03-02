import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):

    words = list(map(str,input()))
    # print(words)
    # ['p', 'r', 'i', 'n', 't', '(', "'", '{', '}', ' ', '{', '}', "'", '.', 'f', 'o', 'r', 'm', 'a', 't', '(', '1', ',', ' ', '2', ')', ')']

    stack = []
    result = 1
    for i in words:
        if i == '(' or i == '{':
            stack.append(i)

        if i == ')' or i == '}':
            if not stack:
                result = 0
                break
            if i == ')':
                if stack[-1] == '(':
                    stack.pop()
                else :
                    result = 0
                    break
            if i == '}':
                if stack[-1] == '{':
                    stack.pop()
                else :
                    result = 0
                    break

    if stack:
        result=0


    print("#{} {}".format(tc,result))