def dfs(idx, n):
    if n == 3:
        comb.sort()
        hunt(comb, 0)
    for i in range(idx, N*M):
        comb.append(tmp[i])
        dfs(i+1, n+1)

def hunt(lst, n):
    global res
    global turns
    if n == 3:
        turns += 1
        turn(lst, turns)
        return
    dis = []
    for i in range(N-1, N-D, -1):
        for j in range(M):
            d = abs(lst[n][0] - i) + abs(lst[n][1] - j)
            if arr[i][j] != 0 and d <= D:
                dis.append((d, i, j))
    dis.sort()
    print(dis)
    ti, tj = dis[0][1], dis[0][2]
    if arr[ti][tj] == 1:
        res += 1
    arr[ti][tj] = -1
    hunt(lst, n+1)

def turn(lst, turnn):
    if turnn == N:
        return
    for i in range(1, N):
        for j in range(M):
            arr[i][j] = arr[i-1][j]
    for i in range(M):
        arr[0][i] = 0
    return

N, M, D = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(N)]
tmp = []
comb = []
res = 0
turns = 0
for i in range(M):
    tmp.append((N, i))
dfs(0,0)
print(res)


