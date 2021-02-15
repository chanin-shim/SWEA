import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N,M = map(int, input().split())
    numbers = list(map(int,input().split()))
    # print(numbers)
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # [6262, 6004, 1801, 7660, 7919, 1280, 525, 9798, 5134, 1821]
    # [3266, 9419, 3087, 9001, 9321, 1341, 7379, 6236, 5795, 8910, 2990, 2152, 2249, 4059, 1394, 6871, 4911, 3648, 1969,
    #  2176]
    sumsum= []
    for i in range(0,len(numbers)): # 0~19까지
        if i < N-M+1:
            aa= 0
            for j in range(M):
                aa += numbers[i+j]
            sumsum += [aa]
    # print(sumsum)
    # [1, 2, 3, 2, 3, 4, 3, 4, 5, 4, 5, 6, 5, 6, 7, 6, 7, 8, 7, 8, 9, 8, 9, 10]
    # [6262, 6004, 1801, 7660, 7919, 6004, 1801, 7660, 7919, 1280, 1801, 7660, 7919, 1280, 525, 7660, 7919, 1280, 525,
    #  9798, 7919, 1280, 525, 9798, 5134, 1280, 525, 9798, 5134, 1821]
    # [3266, 9419, 3087, 9001, 9321, 1341, 7379, 6236, 5795, 8910, 2990, 2152, 2249, 4059, 1394, 6871, 4911, 3648, 1969,
    #  9419, 3087, 9001, 9321, 1341, 7379, 6236, 5795, 8910, 2990, 2152, 2249, 4059, 1394, 6871, 4911, 3648, 1969, 2176]
        my_max = sumsum[0]
        my_min = sumsum[0]
        for num in sumsum:
            if num > my_max:
               my_max = num
        for num2 in sumsum:
            if num2 < my_min:
                my_min = num2
        result = my_max - my_min
    print("#{} {}".format(tc,result))