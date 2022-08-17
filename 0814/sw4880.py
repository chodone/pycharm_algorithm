# 1 - 가위  2 - 바위  3 - 보
# stack 사용
# 1 > 3  , 1 < 2, 3 > 2
# 토너먼트 횟수 - N-1번

def rcp(a,b):
    if a == 1:
        if b == 1:
            return a
        elif b == 2:
            return b


def game(N, lst):



    if N == 1:
        return lst[0]

    elif N == 2:
        pass

    else:
        if not N % 2:
            game(N//2, lst[:N//2])
            game(N//2, lst[N//2:])
        else:
            game(N//2 + 1, lst[:N//2 + 1])
            game(N//2, lst[N//2 + 1:])









TC = int(input())

for tc in range(1, TC+1):
    N = int(input())



    card_lst = list(map(int, input().split()))








