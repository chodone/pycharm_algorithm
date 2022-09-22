import sys
sys.stdin = open('input.txt', 'r')

def solve(k, card):
    global maxV
    if k == N:
        if maxV < card:
            maxV = card
        return
    if card in arrList[k]:
        return
    else:
        arrList[k].append(card)

    #NC2
    card = list(str(card))
    K= len(card)
    for i in range(K-1):
        for j in range(i+1, K):
            card[i], card[j] = card[j], card[i]

            solve(k+1, int(''.join(card)))
            card[i], card[j] = card[j], card[i]



TC = int(input())
for tc in range(1, TC + 1):
    CARD, N = map(int, input().split())

    maxV = 0
    arrList = [[] for _ in range(N)]
    solve(0, CARD)
    print(f'#{tc} {maxV}')