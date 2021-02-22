stack = []

input_string = '()()()()()()()('

for s in input_string:
    if s == '(':
        stack.append(s)
    else:
        if len(stack) == 0: #여는괄호가 더 없다면 애초에 닫는 괄호가 나오면안되니까
            result = False
            break
        stack.pop()
else:
    if len(stack):
        result = False
    else:
        result = True

print(result)