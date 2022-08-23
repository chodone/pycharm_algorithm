def findEnd():
    for i in range(N):
        for j in range(N):
            if mapp[i][j] == 3:
                end.append(i)
                end.append(j)
                return

def DFS(end):
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    ST = []

    cr = end[0]
    cc = end[1]


    while mapp[cr][cc] != 2:
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]

            if not mapp[nr][nc]:
                ST.append((nr, nc))

        if ST:
            return 0

        cr, cc = map(ST.pop())
        mapp[cr][cc] = 1

    return 1














TC = int(input())

for tc in range(1, TC+1):
    N = int(input())

    mapp = [list(map(int, input()))for _ in range(N)]
    visited = [[False] for _ in range(N)]

    end = []


    # 도착점 찾기
    findEnd()

    print(DFS(end))






