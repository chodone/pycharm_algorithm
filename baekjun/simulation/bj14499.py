




N, M, x, y, K = map(int, input().split())
Arr = [list(map(int, input().split()))for _ in range(N)]
orderLst = list(map(int, input().split()))
dice = [0] * 7
diceTwin = {1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}

nToS = [6, 5, 1, 2]
eToW = [3, 4]

for order in orderLst:
    #λ
    if order == 1:
        if 0<= y + 1 < M:
            pass
        else:
            continue

    #μ
    elif order == 2:
        if 0 <= y - 1 < M:
            pass
        else:
            continue

    #λΆ
    elif order == 3:
        if 0 <= x - 1 < M:
            pass
        else:
            continue

    #λ¨
    elif order == 4:
        if 0 <= x + 1 < M:
            pass
        else:
            continue

