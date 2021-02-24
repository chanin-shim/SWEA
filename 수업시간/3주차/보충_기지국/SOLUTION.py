for i in range(N):
    for j in range(N):
        if map[i][j] != 'X' and map[i][j] != 'H': # 기지국일 경우!



    # 인덱스 범위가 넘어가서 에러가 났을 수 있다.

    for k in range(1, ord(map[i][j]) - ord('A') + 2):
        if i + k < N and map[i+k][j] == 'H': #남  # 범위검사를 먼저하고 , 그 다음에 내용물 검사를 해야함. 왜냐면 내용물 먼저검사하면 범위검사할때 터질 수 있음.
            map[i + k][j] = 'X'
        if j + k < N and map[i][j+k] == 'H': #동
            map[i][j+ k] = 'X'
        if i - k > -1 and map[i - k][j] == 'H': #북 #0까지 커버를 해야하기 때문에. i-k >= 0이렇게 해도 좋음.
            map[i - k][j] = 'X'
        if j - k < -1 and map[i][j - k] == 'H': #서
            map[i][j - k] = 'X'