import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    N = int(input())

    my_list = list(input())
    my_tool = '+'
    my_list = my_list[::-1]
    stack = []
    num = 0
    # print(my_list)
    # ['6', '+', '6', '+', '2', '+', '3', '+', '8', '+', '4', '+', '3', '+', '7', '+', '4', '+', '3', '+', '7'
    my_tool_list = []

    while True:
        if not my_list[-1] == my_tool:
            stack.append(int(my_list.pop()))
        else:
            my_tool_list.append(my_list.pop())
            if len(stack) < 2:
                pass
            else:
                my_tool_list.pop()
                stack.append(stack.pop() + stack.pop())
        if not stack:
            break
        if not my_list:
            my_tool_list.pop()
            stack.append(stack.pop() + stack.pop())
            break

    print("#{} {}".format(tc,*stack))