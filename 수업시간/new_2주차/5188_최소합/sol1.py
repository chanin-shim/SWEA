import sys
sys.stdin = open("input.txt")

T = int(input())

def min(n):
    arr[n+1]

def perm(n,k):
    if n == k : print(*nums)
    else:
        for i in range(n, k):
            nums[n], nums[i] = nums[i], nums[n]
            perm(n+1, k)
            nums[n], nums[i] = nums[i], nums[n]

for tc in range(1, T+1):

    nums = [1, 2, 3, 4]
    perm(0, 4)

    print("#{} ".format(tc, ))