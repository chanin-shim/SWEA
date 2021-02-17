def atoi(num_str):
    #최종값을 담을 변수
    value = 0

    for i in range(len(num_str)):
        value *= 10
        value += ord(num_str[i]) - ord('0')

    return value


num_str = '1412412214'

num_int = atoi(num_str)

print(atoi('5325325235'))