import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range (1,T+1):
    words = input()
    result = 1

    stack = []
    for i in range(len(words)):
        if words[i] == '(' or words[i] == '{':
            stack.append(words[i])

        #닫는 괄호가 올 때에도 스택에 저장
        elif words[i] == ')' or words[i] == '}':

            #닫는 괄호가 먼저 와버린 경우
            if len(stack)==0:
                result = 0
                break


            # 스택 안의 저장된 괄호와 일치하지 않는 경우
            if (words[i] == ')' and stack[-1] != '(') or (words[i] == '}' and stack[-1] != '{') :
                result = 0
                break

            else:
                stack.pop()

    if len(stack): # 스택이 비어있지 않다면
        result = 0

    print('#{} {}'.format(tc,result))