import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    my_list = [[] for _ in range (V+1)]
    visited = [0] * (V+1)

    for i in range(E):
        start_node, end_node = map(int, input().split())
        my_list[start_node].append(end_node)
    # print(my_list)

    S, G = map(int,input().split())
    stack = [S]
    result= 0
    while stack:
        now = stack.pop()
        if visited[now]: # 방문 했다면
            pass
        else:
            visited[now] = True
            for i in my_list[now]:
                if not visited[i]:
                    stack.append(i)
                if i == G:
                    result = 1
                    break


    print(result)
