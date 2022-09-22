
def perm(k, midSum, s):
    global minV
    if k == N:
        # sumV = 0
        # for i in range(1, N):
        #     s = result[i-1]
        #     e = result[i]
        #     sumV += Arr[s][e]
        #
        # s = result[N-1]
        # sumV += Arr[s][0]

        midSum += Arr[s][0]
        minV = min(minV, midSum)
        return

    elif midSum > minV:
        return

    for i in range(N):
        if Visited[i]:
            continue
        Visited[i] = True
        perm(k+1, midSum + Arr[s][i], i)
        Visited[i] = False




TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())


    Arr = [list(map(int, input().split())) for _ in range(N)]
    Visited = [False] * N
    Visited[0] = True
    minV = 100000000

    perm(1, 0, 0)
    print(f'#{tc} {minV}')
