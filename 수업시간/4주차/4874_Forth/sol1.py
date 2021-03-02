import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    my_list = list(map(str, input().split()))
    math_tool = ['+','*','/','-','.']
    my_list = my_list[::-1]
    # print(my_list)
    # ['.', '*', '+', '4', '3', '+', '2', '10']

    stack = []
    result = ''
    result2 = ''
    while True:
        if not my_list[-1] in math_tool: # 피 연산자라면
            stack.append(int(my_list.pop())) #스택에 더해줘라

        elif my_list[-1] in math_tool: # 연산자라면
            if my_list[-1] == '+':
                my_list.pop()
                if len(stack) >=2:
                    stack.append(stack.pop() + stack.pop())
                else:
                    result2 = 'error'
            if my_list[-1] == '*':
                my_list.pop()
                if len(stack) >= 2:
                    stack.append(stack.pop() * stack.pop())
                else:
                    result2 = 'error'
            if my_list[-1] == '/':
                my_list.pop()
                if len(stack) >= 2:
                    stack.append(stack.pop() / stack.pop())
                else:
                    result2 = 'error'
            if my_list[-1] == '-':
                my_list.pop()
                if len(stack) >= 2:
                    stack.append(stack.pop() - stack.pop())
                else:
                    result2 = 'error'
            if my_list[-1] == '.':
                my_list.pop()
                result = stack.pop()
                if result2 == 'error':
                    result = 'error'

        if len(my_list) == 0:
            break


    print("#{} {}".format(tc,result))
