import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    print(nums)
    N = nums[0]
    K = nums[1]
    #N은 원소의 갯수, K는 원소의 합

    for i in range(1<<N):
        for j in range(N):
            if i & (1<<j):
                print()


