
def find(r, c, d, back):
    global cnt





    # 청소하기
    if Arr[r][c] == 0:
        Arr[r][c] = 1
        cnt += 1


    # 북
    if d == 0:
        # 서 남 동 북
        dr = [0, 1, 0, -1]
        dc = [-1, 0, 1, 0]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if Arr[nr][nc] == 0:
                find(nr, nc, abs(i-4), False)
                break

        if back:
            return
        else:
            find(r+1, c, d, True)
    # 동
    elif d == 1:
        # 서 남 동 북
        dr = [0, 1, 0, -1]
        dc = [-1, 0, 1, 0]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if Arr[nr][nc] == 0:
                find(nr, nc, abs(i - 4), False)
                break

        if back:
            return
        else:
            find(r + 1, c, d, True)

    #남
    if d == 2:
        # 서 남 동 북
        dr = [0, 1, 0, -1]
        dc = [-1, 0, 1, 0]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if Arr[nr][nc] == 0:
                find(nr, nc, abs(i - 4), False)
                break

        if back:
            return
        else:
            find(r + 1, c, d, True)
    #서
    if d == 3:
        # 서 남 동 북
        dr = [0, 1, 0, -1]
        dc = [-1, 0, 1, 0]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if Arr[nr][nc] == 0:
                find(nr, nc, abs(i - 4), False)
                break

        if back:
            return
        else:
            find(r + 1, c, d, True)


N, M = map(int, input().split())
r, c, d = map(int, input().split())

Arr = [list(map(int, input().split()))for _ in range(N)]
cnt = 0

