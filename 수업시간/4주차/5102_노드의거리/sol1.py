import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    V, E = map(int,input().split())
    edge_list = [[]for _ in range(V+1)]
    # print(edge_list)
    # [[], [4, 3], [3, 5], [], [6], [], []]

    for i in range(E):
        start_node, end_node = map(int,input().split())
        edge_list[start_node].append(end_node)

    S, G = map(int, input().split())

    visited = [0] * (V + 1)
    # [0, 0, 0, 0, 0, 0, 0]

    cnt = 0
    visited = [False] * (V+1)

    while True:
        for i in edge_list[S]: # 4,3
            if visited[i]:
                pass
            else:
                visited[i] = True
                cnt+=1
                for j in range(len(edge_list[i])):
                    if edge_list[i] == G:
                        break
        break






    print("#{} {}".format(tc,cnt))