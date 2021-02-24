import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1,T+1):

    n = int(input())

    my_matrix = [[0 for _ in range(n)]for _ in range(n)]

    my_list = []
    for i in range(n):
        my_list += [input()]
    # print(my_list)
    # ['XXXXXXXXX', 'XXXHXXXXX', 'XXHAHXXHX', 'XXHHXXXXX', 'XXXXXXXXX', 'XXAHHXXXX', 'XXHXXHAHX', 'XXAHXXHXX',
    #  'XXHXHXXXX']

    for i in range(n):
        for j in range(n):
            if my_list[i][j] == 'X':
                'X' == 0
            if my_list[i][j] == 'H':
                'H' == 20 # 어차피 기지국 운좋게 다 겹쳐도 12밖에 안됨.
            if my_list[i][j] == 'A':
                'A' == 0
                my_list[i:i+2][j] += 1
                my_list[i][j:j+2] += 1
                my_list[i-2:i][j] += 1
                my_list[i][j-2:j] += 1
            if my_list[i][j] == 'B':
                my_list[i:i+3][j] += 1
                my_list[i][j:j+3] += 1
                my_list[i-3:i][j] += 1
                my_list[i][j-3:j] += 1
            if my_list[i][j] == 'C':
                my_list[i:i+4][j] += 1
                my_list[i][j:j+4] += 1
                my_list[i-4:i][j] += 1
                my_list[i][j-4:j] += 1

    cnt = 0
    for i in range(n):
        for j in range(j):
            if my_list[i][j] == 20:
                cnt +=1

    print("#{} {}".format(tc,cnt))



# 인덱스에러 어떻게 안뜨게함?