TC = int(input())


for tc in range(1, TC+1):
    K, N, M = map(int, input().split())

    station = [False] * N
    station[0] = True

    charge_station = list(map(int, input().split()))


    for i in charge_station:
        station[i] = True

    charge = True
    cnt = 0
    last = 0

    while charge:
        for stop in range(last+K,last,-1):
            if last+K >= N:
                charge = False
                break

            elif station[stop]:
                cnt += 1
                last = stop
                break

        else:
            cnt = 0
            charge = False


    print(f'#{tc} {cnt}')
















