def find(r, c):
    # 우 좌 하 상
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]

    visited = [[0] * N for _ in range(N)]

    queue = [(r, c)]


    while queue:
        cr, cc = queue.pop(0)

        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]


            if 0 <= nr < N and 0 <= nc < N:
                if Arr[nr][nc] == 0:
                    queue.append((nr, nc))
                    visited[nr][nc] = visited[cr][cc] + 1
                    Arr[cr][cc] = 1
                elif Arr[nr][nc] == 2:
                    return visited[cr][cc]

    return 0








TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())

    Arr = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if Arr[i][j] == 3:
                endR, endC = i, j

    print(f'#{tc} {find(endR, endC)}')




