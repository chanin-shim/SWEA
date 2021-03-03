N = 20 # 마이쮸 갯수

queue = [(1,0)] # 튜플형태로 초기화

# (0,0) [0] = 사람번호, [1] = 직전까지 받았던 마이쮸의 갯수

new_people = 1
last_people = 0

while N > 0 :
    num, cnt = queue.pop(0) #가장 왼쪽거를 가져옴 #받으러온 사람, 저번까지 받은 갯수
    last_people = num # 마지막으로 받으러온 사람
    cnt+=1 # 저번보다는 하나 더 챙겨가자

    N -= cnt # num이라는 친구가 cnt개수만큼 가져감
    new_people += 1

    queue.append((num,cnt)) # 맨 뒤로가서 다시 줄을 섬
    queue.append((new_people, 0)) #새로운 사람도 줄섬
    print(queue)
print(last_people)