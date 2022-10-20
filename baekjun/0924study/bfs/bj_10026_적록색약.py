def normalBfs(r, c):
    global nCnt
    if not nVisited[r][c]:
        nCnt += 1
        nVisited[r][c] = True
        queue = [(r,c)]
        curColor = Arr[r][c]


        # 우 히 좌 상
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]

        while queue:
            cr, cc = queue.pop(0)
            if curColor == 'R':
                Arr[cr][cc] = 'G'

            for i in range(4):
                nr = cr + dr[i]
                nc = cc + dc[i]

                if 0 <= nr < N and 0 <= nc < N and Arr[nr][nc] == curColor and not nVisited[nr][nc]:
                    queue.append((nr, nc))
                    nVisited[nr][nc] = True

    else:
        return









def blindBfs(r,c):
    global dCnt
    if not dVisited[r][c]:
        dCnt += 1
        dVisited[r][c] = True
        queue = [(r, c)]
        curColor = Arr[r][c]

        # 우 히 좌 상
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]

        while queue:
            cr, cc = queue.pop(0)

            for i in range(4):
                nr = cr + dr[i]
                nc = cc + dc[i]

                if 0 <= nr < N and 0 <= nc < N and Arr[nr][nc] == curColor and not dVisited[nr][nc]:
                    queue.append((nr, nc))
                    dVisited[nr][nc] = True

    else:
        return



N = int(input())
Arr = [list(input()) for _ in range(N)]
nVisited = [[False]*N for _ in range(N)]
dVisited = [[False]*N for _ in range(N)]
nCnt = 0
dCnt = 0

for i in range(N):
    for j in range(N):
        normalBfs(i, j)

for i in range(N):
    for j in range(N):
        blindBfs(i, j)

print(nCnt, dCnt)




