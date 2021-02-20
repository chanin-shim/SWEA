import sys
sys.stdin = open("input.txt")

T = int(input())

# 단어를 인식해야, 그 단어의 길이도 아는거아닌가?

for tc in range(1, T+1):
    my_word = input()
    # print((my_word))
    # KOREAKOREAKOREAKOREAKOREAKOREA

    # 아예 스트링 자체로 접근해서
    # 비교했을떄 많이 나오는 문자열중 가장 긴 문자가 단어?

    new_list = []
    for i in range(len(my_word)):
        for j in range(i,len(my_word)):
            new_list += [my_word[i:j]]

    # 이제 여기 new_list에서 가장 자주나오는 단어는 무엇일까?
    # 이걸 어케 구하는 지 모르겠따.

    count_list = []
    true_count = 0
    for i in range(len(new_list)):
        count_list += new_list[i]
        if new_list[i] in count_list == True:
            true_count += 1

















