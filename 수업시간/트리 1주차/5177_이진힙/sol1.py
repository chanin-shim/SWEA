import sys
sys.stdin = open("input.txt")

T = int(input())

def hip(n,idx):
    if tree[idx//2] < n:
        # idx//2 == 부모노드
        # 즉 tree 부모노드에있는 값이 현재 들어오는 값보다 작다면
        tree[idx] = n
        # tree의 지금들어오는 인덱스에 값을 넣어라
    else:
        tree[idx] = tree[idx//2]
        # tree의 지금들어오는 인덱스값에는 트리 부모에 있던 값을 넣고
        hip(n, idx//2)
        # 힙을 부모노드로 다시 돌려라. 그러면 부모노드는

#아직 완벽히 이해간것은 아닌듯.

for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    nums = list(map(int,input().split()))
    index = 1
    total = 0
    for num in nums:
        hip(num, index)
        index += 1
    # print("#{} ".format(tc, ))

    while N > 1:
        N//=2
        total += tree[N]

    print(total)