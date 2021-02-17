import sys
sys.stdin = open("input.txt")

T = int(input())

# 1) 일단 문자를 숫자로
    # 1-1) ZRO:0 으로 해서 딕셔너리에 넣어주자!
    # 1-2) 그다음에 딕셔너리를 기반으로 숫자로 만들기
# 2) 그다음에 정렬
# 3) 그다음에 다시 숫자를 문자로

for tc in range(1,T+1):
    case_num, temp_case_len = map(str, input().split())
    case_len = int(temp_case_len)
    # print(case_num, case_len)
    # 1 7041

    my_dict= {}
    GNS = ["ZRO","ONE","TWO","THR","FOR","FIV","SIX","SVN","EGT","NIN"]

    # GNS 하나씩 꺼내서 숫자와 매칭
    for i in range(len(GNS)):
        my_dict.update({GNS[i]:'{}'.format(int(i))})

    # print(my_dict)
    # {'FOR': '4', 'EGT': '8', 'ONE': '1', 'ZRO': '0', 'FIV': '5', 'NIN': '9', 'SIX': '6', 'THR': '3', 'TWO': '2',
    # 'SVN': '7'}

    case_list = list(map(str,input().split()))
    # print(case_list)
    # ['SVN', 'FOR', 'ZRO', 'NIN', 'FOR', 'EGT', 'EGT', 'TWO', 'FOR', 'FIV', 'FIV', 'ONE', 'SVN', 'ONE', 'ONE', 'FIV',
    # 등등 엄청 나옴

    my_num_list = []

    for i in range(case_len):
        my_num_list += my_dict[case_list[i]]
    # print(my_num_list)
    # ['7', '4', '0', '9', '4', '8', '8', '2', '4', '5', '5', '1', '7', '1']

    my_pure_num_list = []
    for i in range(len(my_num_list)):
        my_pure_num_list += [int(my_num_list[i])]
    my_pure_num_list.sort()
    # print(my_pure_num_list)
    # # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    # # 아 잘 됐구나

    #다시 이제 이거를 my_dict에 넣어서 key값으로 바꿔주면됨
    # 근데 my_dict의 value값이 str여서 다 꼬여버림
    # 다시 my_dict의 value값처럼
    # str으로 만들어서 바꿔줘야함
    str_my_pure_num_list = []
    for i in range(len(my_pure_num_list)):
        str_my_pure_num_list += [str(my_pure_num_list[i])]
    # print(str_my_pure_num_list)
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    # 다시변환성공

    # 이제 이 리스트의 각기항목과
    # 그에 해당하는 my_dict의 key값을 찾으면됨

    # print(my_dict.items())
    # dict_items(
    #     [('ZRO', '0'), ('SVN', '7'), ('FIV', '5'), ('ONE', '1'), ('EGT', '8'), ('SIX', '6'), ('TWO', '2'), ('NIN', '9'),
    #      ('FOR', '4'), ('THR', '3')])

    result = []
    for i in str_my_pure_num_list:
        for key, value in my_dict.items():
            if value == i:
                result += [key]
    # print(result)
    # #['ZRO', 'ZRO', 'ZRO', 'ZRO', 'ZRO', 'ZRO', 'ZRO', 'ZRO', 'ZRO',

    print(case_num)
    for i in result:
        print(i, end=" ")






