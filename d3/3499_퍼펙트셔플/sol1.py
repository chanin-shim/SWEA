import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    card_name = [0]+list(map(str,input().split()))
    # print(card_name)
    # [0, 'A', 'B', 'C', 'D', 'E', 'F']
    # [0, 'JACK', 'QUEEN', 'KING', 'ACE']

    first_deck = []
    second_deck = []
    for i in range(1,len(card_name)):
        if i <= (len(card_name)-1)/2:
            first_deck += [card_name[i]]
        else:
            second_deck += [card_name[i]]

    print(first_deck,second_deck)




    print("#{} ".format(tc, ))