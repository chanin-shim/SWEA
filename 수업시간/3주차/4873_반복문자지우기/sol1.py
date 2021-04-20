# import sys
# sys.stdin = open("input.txt")
#
# T = int(input())
#
#
# for tc in range(1, T+1):
#     my_word = str(input())
#     stack = []
#     for i in range(len(my_word)):
#         stack += my_word[i]
#         if stack[0]:
#             if my_word[i] == my_word[i-1]: # 전거랑 같다면 2개 팝
#                 stack.pop()
#                 stack.pop()
#
#     for i in range(len(stack)-1):
#         if stack[i] == stack[i+1]:
#             stack[i] = 0
#             stack[i+1] = 0
#
#     cnt = 0
#     for i in stack:
#         if i != 0:
#             cnt +=1
#
#     print("#{} {}".format(tc,cnt))
#


    ## 2번째 케이스에서 NNNN 에서 3번째 N부터 해결이 안됨.

import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    my_word = str(input())
    stack = []
    for i in range(len(my_word)):
        if not len(stack) :
            stack += my_word[i]
            continue
        if stack[-1] == my_word[i]:
            stack.pop()
        else:
            stack += my_word[i]


    print("#{} {}".format(tc,len(stack)))