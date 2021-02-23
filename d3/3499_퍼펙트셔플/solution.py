import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    card = input().split()

    print(card)

    mid = len(card)//2 if len(card) % 2 == 0 else len(card)//2 +1
    card1 = [i for i in card[:mid]]
    card2 = [j for j in card[mid:]]

    result = ''
    for c in range(len(card2)):
        result += card1[c] +' '
        result += card2[c] +' '




