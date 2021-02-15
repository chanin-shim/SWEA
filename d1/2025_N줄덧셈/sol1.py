T = int(input())

result = 0
for i in range(1,T+1):
    result += i

print(result)

---

print(total_list)
print(total_list[0])
# total_list를 이차원 리스트로 만듦.



# 각기 최대값들 변수 초기화
for tc in range(T):
    max_width_sum = 0
    max_height_sum = 0
    diagnal_1 = 0
    diagnal_2 = 0

    # 가로길이 구하기
    for i in range(len(total_list)):
        width_sum = 0
        for j in range(len(total_list[0])):
            width_sum += total_list[i][j]
            if width_sum > max_width_sum:
                max_width_sum = width_sum

    # 세로길이 구하기
    for i in range(len(total_list[0])):
        height_sum = 0
        for j in range(len(total_list)):
            height_sum += total_list[j][i]
            if height_sum > max_height_sum:
                max_height_sum = height_sum

    # 우하향 대각선 구하기
    for i in range(len(total_list)):
        for j in range(len(total_list[0])):
            if i == j:
                diagnal_1 += total_list[i][j]

    # 좌하향 대각선 구하기
    for i in range(len(total_list[0]) - 1, -1, -1): # i = 99 ~ 0까지 -1씩 내려감
        for j in range(len(total_list)): # 0~99
            if i+j == 99:
                diagnal_2 += total_list[j][i]

    # 구한 각각의 합을 final_list에 넣어서
    # 가장 큰 값을 비교하여 구하기
    final_list = [max_height_sum, max_width_sum, diagnal_1, diagnal_2]
    result = final_list[0]
    for i in final_list:
        if i > result:
            result = i

    # 1) 일단 다 받아서 2차원 리스트 100x100의 형태로 만든다 (애초에 2차원 리스트로 어케 받아옴??)
    # 2) 그리고 행으로 for문돌려서 sum구하고
    # 3) 열로 for for문 구해서 sum 구하고
    # 4) 대각선은 i=j해서 구하고
    # 5) 반대 대각선은 i-1, j+1로 해서 구하고
    # 6) 비교

    print("#{} {}".format(tc, result))