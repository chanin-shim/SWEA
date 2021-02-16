my_list = ['+'] * 5
# my_list 가 없으면 안돌아가서 일단 만듦.
​
for i in range(len(my_list)):
    my_list = ['+'] * 5
    # ['+','+','+','+','+'] 리스트를 만듦
    my_list[i] = '#'
    # i자리의 +를 #으로 교체
    my_word = ''
    # 결과값을 담을 수 있는 빈 스트링
    for j in my_list:
        my_word += j
        #리스트의 원소들을 하나씩 꺼내서 my_word로 str으로 묶어줌
        if len(my_word) % 5 == 0:
        # 리스트의 원소가 5개가 채워지면
            print(my_word,end="\n")
            #my_word를 출력하고 한 줄 띈다.