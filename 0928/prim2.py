def prim2(r,N):         # r = 시작 번호 , N = 마지막 번
    U = [0] * (N+1)     # MST 포함여부
    U[r] = 1
    S = 0               # 가중치의 합

    for _ in range(N):
        u = 0
        minV = 1e10
        for i in range(N+1):
            if U[i] == 1:
                for j in range(N+1):
                    if G[i][j] > 0 and U[j] == 0 and minV>G[i][j]:
                        u = j                   # 최소 가중치 연결 노드 기억
                        minV = G[i][j]          # 최소 가중치를 찾기 위해 minV update

        S += minV                   # 구한 최소가중치를 가중치의 합에 더하기
        U[u] = 1                    # 최소 가중치로 연결된 노드를 MST에 기록 -> 이 노드는 확정된 노드라고 생각

    return S





N, E = map(int, input().split())
G = [[1000000] * (N+1) for _ in range(N+1)]
for _ in range(E):
    n1, n2, w = map(int, input().split())
    G[n1][n2] = w
    G[n2][n1] = w

print(prim2(0, N))
