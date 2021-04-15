import sys
sys.stdin = open("input.txt")

T = int(input())

openparenthesis = {
    '[': ']',
    '{': '}',
    '(': ')'
}

closeparenthesis = {
    ']': '[',
    '}': '{',
    ')': '('
}
# for i,v in openparenthesis.items():
#     closeparenthesis[v] = i

def Valid(word):
    stack = []
    global result
    for char in my_words:
        if char in openparenthesis:
            stack.append(char)
        elif char in closeparenthesis:
            if len(stack) == 0 or stack[-1] !=closeparenthesis[char]: # 스택에 하나도 없거나, 스택의 마지막에 들어있는게 매칭되는 괄호가 아니라면
                result = 0
                return
            else:
                stack.pop()

            return len(stack) == 0


for tc in range(1, T+1):

    my_words = input().split()
    result = 0
    Valid(my_words)
    print(result)