# # 5 * 2^3
# # a << n = a * 2^n
#
# arr = [3,6,7,1,5,4]
#
# n = len(arr)
# #6
#
# print(n)
# #64
#
# for i in range(1<<n): # 0 ~63 #여기서 나오는 i를 2진법으로 생각해여함 0001 처럼
#     for j in range(n):
#         if i & (1<<j):
#             print(arr[j], end=", ")
#     print()
# print()
#
#
#

print(81<<4)