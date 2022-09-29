def dijk():
    U = []
    D = [10000] * (N + 1)
    P = [10000] * (N + 1)
    D[0] = 0
    while len(U) < (N+1):

        # D최솟값을 구한다.
        minV = 10000

        for i in range(N + 1):
            if i in U: continue
            if minV > D[i]:
                minV = D[i]
                curV = i

        U.append(curV)

        #D를 업데이트
        for i in range(N + 1):
            if i in U: continue
            # if G[curV][i] and D[i] > D[curV] + G[curV][i]:
            #     D[i] = D[curV] + G[curV][i]
            # if G[curV][i]:
            D[i] = min(D[i], D[curV] + G[curV][i])
            P[i] = curV

    print(U, D, P)



N, E = map(int, input().split())
G = [[100000] * (N + 1) for _ in range(N + 1)]
for i in range(E):
    n1, n2, w = map(int, input().split())
    G[n1][n2] = w
    # G[n2][n1] = w
# print(G)
# prim()
dijk()

