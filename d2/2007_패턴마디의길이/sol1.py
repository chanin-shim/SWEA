# import sys
# sys.stdin = open("input.txt")
#
# T = int(input())
#
# # 마디의 길이! 를 알아내는 문제
# # 알파벳 (A:1)이렇게 딕셔너리에 넣어놓고
# # [0] * 26만들어서 공통적으로 높은 숫자가 있을텐데
# # 그것들의 갯수를 적기

\\
#
# # 완전히 틀린 접근방식이었음.
# # samsung처럼 s가 중복되면 단어를 찾지를 못함.
# alp_dict = { 'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,
#              'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
#
# for tc in range(1, T+1):
#
#     alp_list = [0 for _ in range(len(alp_dict))]
#     my_word = input()
#     # print(my_word)
#     # KOREAKOREAKOREAKOREAKOREAKOREA
#
#     for i in my_word:
#         alp_list[alp_dict[i]-1] += 1
#
#     print(alp_list)
