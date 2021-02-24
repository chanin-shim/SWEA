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
    second_dect = []

    for i in range(1,len(card_name)):
        if i<=len(card_name)//2:
            first_deck.append([card_name[i]])
        else:
            second_dect.append([card_name[i]])

    # print(first_deck, '<->', second_dect)

    suffle_deck = []
    for i in range(len(first_deck)):
        suffle_deck += first_deck[i]
        if i >= len(second_dect):
            pass
        else:
            suffle_deck += second_dect[i]

    # print(suffle_deck)
    # ['A', 'D', 'B', 'E', 'C', 'F']
    # ['JACK', 'KING', 'QUEEN', 'ACE']

    word_sum = ''
    for i in suffle_deck:
        word_sum += i + ' '


    print("#{} {}".format(tc,word_sum))