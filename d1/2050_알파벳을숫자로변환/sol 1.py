import sys
sys.stdin = open("input.txt")

words = input()
# print(words)
# # ABCDEFGHIJKLMNOPQRSTUVWXYZ

# print(words[0])
# A
# 문자열을 []주고 꺼낼 수 있구나!

total = {}
# 빈 딕셔너리 하나 만듦

for i in range(1,len(words)+1):
    total.update({"{}".format(words[i-1]):"{}".format(i)})
# 1~26까지 숫자를 돌리면서 words[0~25]를 1~26까지와 매칭시켜줌
# print(total)
# {'W': '23', 'X': '24', 'S': '19', 'U': '21', 'T': '20', 'Q': '17', 'V': '22', 'I': '9', 'D': '4', 'Y': '25', 'O': '15', 'J': '10', 'A': '1', 'N': '14', 'C': '3', 'H': '8', 'F': '6', 'L': '12', 'M': '13', 'K': '11', 'Z': '26', 'B': '2', 'P': '16', 'G': '7', 'E': '5', 'R': '18'}


# print(total["A"])
# 1

for i in range(1, len(words)+1):
    print(int(total[words[i-1]]), end=" ")
# words[0]이 A이기 때문에 I-1해서 돌려줌.

# 왜 틀린거지?