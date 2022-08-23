def rsp(st, en):
    if card_lst[st-1] == 1:
        if card_lst[en-1] == 1:
            return st
        elif card_lst[en-1] == 2:
            return en
        else:
            return st
    elif card_lst[st-1] == 2:
        if card_lst[en-1] == 1:
            return st
        elif card_lst[en-1] == 2:
            return st
        else:
            return en
    elif card_lst[st-1] == 3:
        if card_lst[en-1] == 1:
            return en
        elif card_lst[en-1] == 2:
            return st
        else:
            return st

def winner(st, en):


    if en - st == 1:
        return rsp(st, en)

    else:
        winner(st, (st+en) // 2)
        winner((st+en)//2 + 1, en)




TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    card_lst = list(map(int, input().split()))

    st = 1
    en = N

    winner(st, en)
