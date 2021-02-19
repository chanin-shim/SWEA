import sys

sys.stdin = open()

def 브루트포스1(p,t):
    #for문

    for i in range(len(t)-len(p)+1):
        #패턴의 길이만큼 반복
        is_ok = True #for else 구문이 생각나지 않을때 변수를 활용
        for j in range(len(p)):
            if p[j] != t[i+j]:
                is_ok = False
                break
        # else:
        #   return 1
        if is_ok:
            return 1


def 브루트 포스 2 (p,t):
    i = 0 # t텍스트를 컨트롤 하는 인덱스
    j = 0 # p패턴을 컨트롤하는 인덱스

    # j가 패턴의 길이가 된다면 찾았다면 멈춘다.
    # i가 텍스트의 길이가 되면 멈춘다.
    while j < len(p) and i < len(t):
        if p[j] != t[i]:
            i = i-j #시작위치로 돌아가고
            j = -1 #

        i += 1
        j += 1

    #패턴을 찾았다.
    if j == len(p): return 1
    else: return 0