def charge(busStop, batVol, cnt):
    global minCnt
    if busStop == N:
        if minCnt > cnt:
            minCnt = cnt
        return

    elif batVol == 0 or cnt >= minCnt:
        return


    for i in range(batVol, 0, -1):
        nBusStop = busStop + i
        if nBusStop <= N:
            charge(nBusStop, batInfo[nBusStop-1], cnt + 1)




TC = int(input())

for tc in range(1, TC + 1):
    lst = list(map(int, input().split()))
    N = lst[0]
    batInfo = lst[1:] + [0]
    minCnt = 1e10


    charge(1, batInfo[0], 0)



    print(f'#{tc} {minCnt-1}' )