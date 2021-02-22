import sys
sys.stdin = open("input.txt")

T = int(input())

def reverse_string(word):
    reverse_word = ''
    for i in range(len(word)-1,-1,-1):
        reverse_word += word[i]
    return reverse_word


for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N = 글자판 크기 n*n
    # M = 회문의 길이 (길이가 M)

    #가로찾기
    ans = ''
    col_list = []
    for i in range(N):
        my_text = str(input())
        col_list.append(my_text)
        for j in range(len(my_text)):
            for l in range(j+1,len(my_text)+1):
                if len(my_text[j:l]) == M:
                    if my_text[j:l] == reverse_string(my_text[j:l]):
                        ans = my_text[j:l]

    # print(col_list)
    # ['GOFFAKWFSM', 'OYECRSLDLQ', 'UJAJQVSYYC', 'JAEZNNZEAJ', 'WJAKCGSGCF', 'QKUDGATDQL', 'OKGPFPYRKQ', 'TDCXBMQTIO',
    #  'UNADRPNETZ', 'ZATWDEKDQF']


    #세로찾기
    new_col_list = []

    for i in range(len(col_list[0])):
        new_col_str = ''
        for j in range(len(col_list)):
            new_col_str += col_list[j][i]
        new_col_list += [new_col_str]

    # print(new_col_list)
    # ['GOUJWQOTUZ', 'OYJAJKKDNA', 'FEAEAUGCAT', 'FCJZKDPXDW', 'ARQNCGFBRD', 'KSVNGAPMPE', 'WLSZSTYQNK', 'FDYEGDRTED',
    #  'SLYACQKITQ', 'MQCJFLQOZF']

    for i in range(len(new_col_list)): # 0 ~ 9
        for j in range(len(new_col_list[i])): # 0 ~ 9
            for k in range(j,len(new_col_list[i])+1):  # j ~ 10
                if len(new_col_list[i][j:k]) == M:
                    if new_col_list[i][j:k] == reverse_string(new_col_list[i][j:k]):
                        ans = new_col_list[i][j:k]
    print("#{} {}".format(tc,ans))