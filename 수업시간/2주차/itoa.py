def itoa(my_int):
    # ord 함수 사용하여 아스키 코드 값으로 변환
    my_str = []

    while my_int != 0:
        r = my_int % 10
        num = chr(ord('0')+r)
        my_str.append(num)
        my_int //= 10
        # 위 식은 my_int = my_int // 10과 같음
        # 10으로 나눈 몫을 자기 자신에게 준다.
    # print(my_str)
    # ['3', '2', '1']
    #하나 하나 쪼갠값을 글자로 출력한거

    my_str.reverse()
    return ''.join(my_str)

print(itoa(123), type(itoa(123)))


