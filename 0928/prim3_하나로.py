def prim(G):
    U = [False] * N
    D = [1000000000000] * N
    D[0] = 0

    for _ in range(N):
        # curV=U에 D중 가장 작은 값을 가진 정점 선택
        minV = 1000000000000
        for i in range(N):
            if U[i]:
                continue
            if minV > D[i]:
                minV = D[i]
                curV = i

        U[curV] = True
        # curV하고 연결된 정점들의 D값을 최선으로 바꿔준다
        for i in range(N):
            if U[i]:
                continue
            if D[i] > G[curV][i]:
                D[i] = G[curV][i]
    result = 0
    for d in D:
        result += d
    return result * E


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    x_lst = list(map(int, input().split()))
    y_lst = list(map(int, input().split()))
    E = float(input())
    node = [[0] * (N) for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            dist = (x_lst[i] - x_lst[j]) ** 2 + (y_lst[i] - y_lst[j]) ** 2
            node[i][j] = dist
            node[j][i] = dist
    print(f'#{tc} {round(prim(node))}')
