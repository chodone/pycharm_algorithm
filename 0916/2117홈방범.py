
def find(row, col):
    dis = [0] * (2*N+1)
    for hRow, hCol in HOMES:
        # 시작지점으로부터 home까지의 거리를 계산하여 dis에 count
        t = abs(hRow-row) + abs(hCol-col)
        dis[t] += 1

    maxNum = 0
    for k in range(1, 2*N+1):
        numH = sum(dis[:k])
        if numH * M - (경비) >= 0 and maxNum < numH:
            maxNum = numH
    return maxNum


TC = int(input())

for tc in range(1, TC + 1):
    N, M = map(int, input())
    CITY = []
    HOMES = []
    for r in range(N):
        for c in range(N):
            if CITY[r][c] == 1:
                HOMES.append((r,c))

    for row in range(N):
        for col in range(N):
            result = find(row, col)
            if maxV < result:
                maxV = result