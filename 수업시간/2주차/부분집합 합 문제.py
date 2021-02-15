# 집합의 원소가 n개 일때, 공집합을 포함한 부분집합의 수는 2^n개 이다.
# 포함하거나 안하거나 2가지의 경우를 모든 원소에 적용한 경우이기 때문에

bit = [0,0,0,0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print(bit)