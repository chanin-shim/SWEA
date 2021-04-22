import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    words = input().split()
    calculation = ['+','-','*','/']
    stack = []
    result = 0
    for i in range(len(words)):
        if words[i] in calculation: # 연산기호일 때
            if not len(stack):
                break
            else:
                try:
                    bb = stack.pop()
                    aa = stack.pop()
                    if words[i] == '+':
                        stack.append(aa + bb)
                    if words[i] == '*':
                        stack.append(aa * bb)
                    if words[i] == '/':
                        stack.append(int(aa / bb))
                    if words[i] == '-':
                        stack.append(aa - bb)

                except:
                    result = 'error'

        elif words[i] == '.':
            break

        else: # 숫자일때
            n = int(words[i])
            stack.append(n)




    try:
        result = stack[0]
    except:
        result = 'error'

    print("#{} {}".format(tc, result))



    # tc 하나 틀렸다고 나오는데 왜와이? 모르겠음.