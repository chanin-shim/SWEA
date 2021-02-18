# import sys
# sys.stdin = open("input.txt")
#
# T = int(input())
#
# # 1) goal_list 리스트에 모든 숫자를 넣어놓음.
# # 2) 10으로 나눠서 각 자리수 별로 숫자 구해줌
# # 3) my_list와 goal_list비교해서 다 있으면 멈춤
# # 4) count 세어서 출력
#
# for tc in range(1, T+1):
#
#     start_num = int(input())
#
#     # print(N)
#
#     goal_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#     my_list = []
#     cnt = 0
#     while cnt < 512:
#         cnt += 1
#         while True:
#             my_list.append(start_num % 10)
#             start_num = start_num // 10
#             if start_num // 10 == 0:
#                 break
#         start_num = +1
#
#         if goal_list == my_list:
#             break
#
#     print(cnt)
#
#     print("#{} ".format(tc, ))
#
#
#
#
# ###################################
#
# import sys
# sys.stdin = open("input.txt")
#
# T = int(input())
#
# for tc in range(1, T+1):
#     my_list = [0] * 10
#     start_num = int(input())
#
#     # print(my_list)
#     # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#
#         cnt = 0
#         while cnt < 5125:
#             cnt += 1
#             while True:
#                 my_list[start_num % 10] += 1
#                 start_num = start_num // 10
#                 for i in my_list:
#                     i
#                     break
#             start_num = +1
#
#
#     print("#{} ".format(tc, ))
nums = set()
print(type(nums))
print(nums)
nums.add(4)
print(nums)