def prim(r,N):
    MTS = [0] * N
    MTS[r] = 1
    s = 0
    lst = []

    for _ in range(N-1):
        u = 0
        minV = 1e10
        for i in range(N):
            if MTS[i] == 1:
                for j in range(N):
                    if G[i][j] and not MTS[j] and minV > G[i][j]:
                        u = j
                        minV = G[i][j]
                lst.append(minV)

        s += minV
        MTS[u] = 1


    return s

TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())
    G = [[0] * N for _ in range(N)]

    xLst = list(map(int, input().split()))
    yLSt = list(map(int, input().split()))

    E = float(input())

    for i in range(N):
        for j in range(i+1 , N):
            G[i][j] = ((xLst[i] - xLst[j])**2 + (yLSt[i] - yLSt[j])**2)*E
            G[j][i] = ((xLst[i] - xLst[j])**2 + (yLSt[i] - yLSt[j])**2)*E


    print(round(prim(0,N)))




