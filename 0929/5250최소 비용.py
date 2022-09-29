from collections import deque


def bfs(r, c):
    global res

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    q = deque()

    q.append((r,c))
    dis[0][0] = 0

    while q:
        cr, cc = q.popleft()
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            curV = dis[cr][cc]




            if 0 <= nr < N and 0 <= nc < N:
                if Arr[nr][nc] > Arr[cr][cc]:
                    curV += Arr[nr][nc] - Arr[cr][cc] + 1
                else:
                    curV += 1
                if dis[nr][nc] > curV:
                    dis[nr][nc] = curV
                    q.append((nr, nc))










TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())
    Arr = [list(map(int, input().split())) for _ in range(N)]
    dis = [[1000000] * (N) for _ in range(N)]


    bfs(0,0)

    print(f'#{tc} {dis[N-1][N-1]}')
