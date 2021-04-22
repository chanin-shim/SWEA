import sys
sys.stdin = open("input.txt")

T = int(input())

def search(last_node):


    for tc in range(1, T+1):
        V, E = input().split()
        V = int(V)
        E = int(E)

        my_map = [list(map(int,input().split())) for _ in range(E)]
        # [
        # [0, 1, 9],
        # [0, 2, 3],
        # [0, 3, 7],
        # [1, 4, 2],
        # [2, 3, 8],
        # [2, 4, 1],
        # [3, 4, 8]
        # ]

        my_tree = [[] for _ in range(E+1)]
        my_w = [[] for _ in range(E+1)]
        # print(my_tree)
        # [[], [], [], [], [], [], [], []]
        for i in my_map:
            n1 = i[0]
            n2 = i[1]
            w = i[2]

            my_tree[n1] += [n2]
            my_w[n1] += [w]

        print('my_tree = ', my_tree)
        print('my_w = ', my_w)
        # print("#{} ".format(tc, ))

        search(V)