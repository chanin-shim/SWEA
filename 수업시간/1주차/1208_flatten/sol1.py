import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    dump_number = int(input())
    # print(dump_number)
    # 834
    box_height_list = list(map(int,input().split()))
    # print(box_height_list)
    # [42, 68, 35, 1, 70, 25, 79, 59, 63, 65, 6, 46, 82, 28, 62, 92, 96, 43, 28, 37, 92, 5, 3, 54, 93, 83, 22, 17, 19, 96, 48, 27, 72, 39, 70, 13, 68, 100, 36, 95, 4, 12, 23, 34, 74, 65, 42, 12, 54, 69, 48, 45, 63, 58, 38, 60, 24, 42, 30, 79, 17, 36, 91, 43, 89, 7, 41, 43, 65, 49, 47, 6, 91, 30, 71, 51, 7, 2, 94, 49, 30, 24, 85, 55, 57, 41, 67, 77, 32, 9, 45, 40, 27, 24, 38, 39, 19, 83, 30, 42]

    cnt = 0
    while cnt< dump_number:
        cnt +=1
        for i in range((len(box_height_list))-1,-1,-1):
            for j in range(0,i):
                if box_height_list[j] > box_height_list[j+1]:
                    box_height_list[j],box_height_list[j+1] = box_height_list[j+1], box_height_list[j]
        box_height_list[0] += 1
        box_height_list[len(box_height_list)-1] -= 1

    max_num = 0
    min_num = box_height_list[0]
    for i in box_height_list:
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i

    ans = max_num - min_num



    print("#{} {}".format(tc,ans))