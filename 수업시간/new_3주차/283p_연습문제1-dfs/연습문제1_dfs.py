import sys
sys.stdin = open("input.txt")

T = 1

# def DFS(s):
#     global result
#     stack.append(s)
#     result += [s]
#     while len(stack):
#         v = stack.pop()
#         visited[v] = True
#         for i in range(len(my_matrix)):
#             for j in range(len(my_matrix[0])):
#                 if my_matrix[i][j] != 0:
#                     if not visited[j]:
#                         stack.append(j)
#                         result += [j]

# def DFS(s):
#     visited[s] = True
#     for i in range(len(my_matrix)):
#         for j in range(len(my_matrix[0])):
#             if my_matrix[i][j] != 0:
#                 if not visited[j]:
#                     print(j)
#                     DFS(j)

def DFS(s):
    visited[s] = True
    print(s)
    for i in range(1,V+1):
        if my_matrix[s][i] != 0:
            if not visited[i]:
                DFS(i)




for tc in range(1,T+1):

    nums = list(map(int,input().split()))
    # print(nums)
    # [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
    E = len(nums) // 2  # 간선의 수
    V = 7
    my_matrix = [[0 for _ in range(V + 1)] for _ in range(V + 1)]

    for i in range(E):
        n1 = nums[i*2]
        n2 = nums[i*2+1]
        my_matrix[n1][n2] = 1

    # for i in range(1, V+1):
    #     for j in range(1, V+1):
    #         if my_matrix[i][j]:
    #             print(i,j)

    s = 1
    visited = [0] * (V+1)
    stack = []
    result = []
    DFS(s)

    print(my_matrix)



