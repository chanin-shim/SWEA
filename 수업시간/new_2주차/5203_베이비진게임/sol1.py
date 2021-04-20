import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    cards = list(map(int,input().split()))
    a_player = []
    b_player = []
    result = 0

    for i in range(len(cards)):
        if i%2 == 0: # 처음에 a가 시작
            cnt_run = 0
            triplet_set = set()
            triplet_set_left = set()
            triplet_set_right = set()
            a_player += [cards[i]]
            for j in a_player: # a플레이어가 든걸 하나씩 꺼내서
                if j == cards[i]: # 이번에 들어온 카드랑 같다면 cnt_run 더해주기
                    cnt_run +=1
                    if cnt_run == 3: # 총 3장이 같다고 나오면
                        result = 1 # 승리
                if j == cards[i]-1 or j == cards[i]+1 : # 이번에 뽑은 카드보다 -1, 또는 +1 인 카드가 있다면
                    triplet_set.add(j) # set에 더해줌
                    if len(triplet_set) == 2: # 그런 것이 중복없이 2개 있다면
                        result = 1 # 승리
                if j == cards[i]-1 or j == cards[i]-2 : # 이번에 뽑은 카드보다 -1, 또는 -2 인 카드가 있다면
                    triplet_set_left.add(j) # set에 더해줌
                    if len(triplet_set_left) == 2: # 그런 것이 중복없이 2개 있다면
                        result = 1 # 승리
                if j == cards[i]+1 or j == cards[i]+2 : # 이번에 뽑은 카드보다 +1, 또는 +2 인 카드가 있다면
                    triplet_set_right.add(j) # set에 더해줌
                    if len(triplet_set_right) == 2: # 그런 것이 중복없이 2개 있다면
                        result = 1 # 승리
        else:
            cnt_run = 0
            triplet_set = set()
            b_player += [cards[i]]
            for j in b_player: # b플레이어가 든걸 하나씩 꺼내서
                if j == cards[i]: # 이번에 들어온 카드랑 같다면 cnt_run 더해주기
                    cnt_run +=1
                    if cnt_run == 3: # 총 3장이 같다고 나오면
                        result = 2 # 승리
                if j == cards[i]-1 or j == cards[i]+1 : # 이번에 뽑은 카드보다 -1, 또는 +1 인 카드가 있다면
                    triplet_set.add(j) # set에 더해줌
                    if len(triplet_set) == 2: # 그런 것이 중복없이 2개 있다면
                        result = 2 # 승리
                if j == cards[i]-1 or j == cards[i]-2 : # 이번에 뽑은 카드보다 -1, 또는 -2 인 카드가 있다면
                    triplet_set_left.add(j) # set에 더해줌
                    if len(triplet_set_left) == 2: # 그런 것이 중복없이 2개 있다면
                        result = 2 # 승리
                if j == cards[i]+1 or j == cards[i]+2 : # 이번에 뽑은 카드보다 +1, 또는 +2 인 카드가 있다면
                    triplet_set_right.add(j) # set에 더해줌
                    if len(triplet_set_right) == 2: # 그런 것이 중복없이 2개 있다면
                        result = 2 # 승리



    print("#{} {}".format(tc,result))


    # 단순하게 5가나왔을때 4,6이 있으면 정답으로 해라는 하겠는데
    # 4가나왔을때 4,5,6이 되면 답이 되라는 못하겠다.

    # 또한 0이면, 9다음 숫자로도 연결된다는 것도 써줘야함.