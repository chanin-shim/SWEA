import sys
sys.stdin = open("input.txt")

T = 10

for _ in range(1, T+1):
    tc, E = list(map(int, input().split()))

    edge_matrix = [[0 for _ in range(100)] for _ in range(100)]
    edge_input = list(map(int, input().split()))
    # print(edge_input)
    # [0, 1, 0, 2, 1, 4, 1, 3, 4, 8, 4, 3, 2, 9, 2, 5, 5, 6, 5, 7, 7, 99, 7, 9, 9, 8, 9, 10, 6, 10, 3, 7]

    for i in range(E):
        start_node = edge_input[i*2]
        end_node = edge_input[i*2+1]

        edge_matrix[start_node][end_node] =1


    visited = [False] * 100
    stack = [0]

    while stack:
        now = stack.pop()

        #방문을 안했을 때가 중요한 것임.
        if not visited[now]:
            visited[now] = True

            for v in range(100):
                if not visited[v] and edge_matrix[now][v] == 1:
                    stack.append(v)


    result = 1 if visited[99] else 0

    print("#{} {}".format(tc, result))