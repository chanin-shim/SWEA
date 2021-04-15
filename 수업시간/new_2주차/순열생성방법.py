def perm(n,k):
    if n == k : print(*nums)
    else:
        for i in range(n, k):
            nums[n], nums[i] = nums[i], nums[n]
            perm(n+1, k)
            nums[n], nums[i] = nums[i], nums[n]

nums = [1,2,3,4]
perm(0,4)