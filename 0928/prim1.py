


from pprint import pprint


# V, E = map(int, input().split())
# adjM = [[0] * (V+1) for _ in range(V+1)]
# adjL = [[] for _ in range(V+1)]
#
# for _ in range(E):
#     u, v, w = map(int, input().split())
#     adjM[u][v] = w
#     adjM[v][u] = w
#     adjL[u].append((v, w))
#     adjL[v].append((u, w))

'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''


def prim():
    U = []      # MST 포함 여부
    D = [10000] * (N + 1)    # 가중치의 최대값 이상으로 초기화 ,
    P = [10000] * (N + 1)
    D[0] =0
    while len(U) < N+1:
        # curV=U에 D중 가장 작은 값을 가진 정점 선택
        # D에서 최소를 구한다. (단, U에 포함되지 않은 것을 대상으로)
        minV = 10000
        for i in range(N + 1):
            if i in U: continue
            if minV > D[i]:
                minV = D[i]
                curV = i

        U.append(curV)
        # curV하고 연결된 정점들의 D값을 최선으로 바꿔준다
        for i in range(N + 1):
            if i in U: continue
            if D[i] > G[curV][i]:
                D[i] = G[curV][i]
                P[i]=curV
    print(U,D, P)
    print(sum(D))


N, E = map(int, input().split())      # 노드의 수가 6이라면 0까지 포함하므로 총 개수는 7개
G = [[1000000] * (N + 1) for _ in range(N + 1)]
for i in range(E):
    n1, n2, w = map(int, input().split())
    G[n1][n2] = w
    G[n2][n1] = w
pprint(G)
prim()