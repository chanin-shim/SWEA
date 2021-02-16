import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):

    test_num = int(input()) # 시행 횟수 값 = tc
    student_list = list(map(int, input().split())) # 학생들 점수 담긴 리스트

    # print(student_list)
    # [41, 85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67, 51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64, 52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24, 51, 15, 13, 39, 67, 97, 19, 76, 12, 33, 99, 18, 92, 35, 74, 0, 95, 71,
    # 등등 준나 많음

    #my_list 초기화
    my_list = [0] * 1000

    # student_list에서 하나씩 요소를 꺼내와서
    # ex) 41,85, 72
    # my_list[45] 번째 값에 값을 1씩 올려줌. 45점이 한명 있었다는 뜻
    for i in student_list:
        my_list[i] += 1
    #print(my_list)
    #[12, 15, 9, 12, 15, 9, 10, 10, 11, 11, 8, 10, 10, 15, 13, 7, 10, 8, 10, 10, 13, 15, 16, 7, 14, 10, 13, 2, 10, 8, 8, 8, 15, 12, 15, 13, 5, 3, 13
    # 등등 준나 많음
    # 음 잘 들어갔군!

    common_num = my_list[0]
    for i in my_list:
        if i > common_num:
            common_num = i
    # 위의 식은 틀림. 이건 얼마나 자주 나왔는지 횟수를 보여주는 것임
    # 출력값은 가장 자주 나온 값이 뭐였는지를 알아야함.
    # 즉 common_num이 나온 것의 인덱스값을 알아야함.

    max_num = my_list.index(common_num)
    # print(max_num)
    # 71

    # 이때 최빈수가 여러 개 일 때, 가장 큰 점수를 출력해야함.
    final_max_num = 0
    for i in range(len(my_list)):
        if my_list[i] == common_num:
            final_max_num = i
    # i는 뒤쪽까지 (0~999)까지 다 찾아보기 때문에
    # 어차피 마지막에 common_num과 일치하는 값이 (가장 큰 값이)
    # final_max_num 으로 나오게 될 것 임.


    print("#{} {}".format(test_num,final_max_num))

