def bfs(start):

    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]

    queue = [start]

    while queue:
        cr, cc = queue.pop(0)
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]

            if 0 <= nr < 16 and 0 <= nc < 16:
                if Arr[nr][nc] == 0:
                    queue.append((nr, nc))
                    Arr[cr][cc] = 1
                elif Arr[nr][nc] == 3:
                    return 1


    return 0



def findS():

    for i in range(16):
        for j in range(16):
            if Arr[i][j] == 2:
                return i, j





TC = 10

for tc in range(1, TC+1):
    N = input()

    Arr = [list(map(int, input()))for _ in range(16)]

    start = findS()




    print(f'#{tc} {bfs(start)}')