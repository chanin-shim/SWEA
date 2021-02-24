import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    length = int(input())

    nums = list(input())
    # print(num)
    # ['9', '+', '8', '+', '5', '+', '9', '+', '2', '+', '4', '+', '1', '+', '8',
    stack = []
    int_list = []
    for i in range(len(nums)) :
        if i % 2 == 0:
            int_list += [int(nums[i])]
        else :
            stack += nums[i]

    int_list.pop()




    print("#{} ".format(tc, ))