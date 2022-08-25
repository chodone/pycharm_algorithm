

def funA(row, col):
    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]

    cr, cc = row, col

    for i in range(4):
        nr = cr + dr[i]
        nc = cc + dc[i]
        if 0<= nr < N+1 and 0 <= nc < N:
            if Arr[nr][nc] == 'H':
                Arr[nr][nc] = '-'






def funB(row, col):
    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]

    cr, cc = row, col

    for j in range(2):
        for i in range(4):

            nr = cr + dr[i]*(j+1)
            nc = cc + dc[i]*(j+1)

            if 0 <= nr < N + 1 and 0 <= nc < N:
                if Arr[nr][nc] == 'H':
                    Arr[nr][nc] = '-'

def funC(row, col):
    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]

    cr, cc = row, col

    for j in range(3):
        for i in range(4):
            nr = cr + dr[i] * (j + 1)
            nc = cc + dc[i] * (j + 1)

            if 0 <= nr < N + 1 and 0 <= nc < N:
                if Arr[nr][nc] == 'H':
                    Arr[nr][nc] = '-'


TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())




    Arr = [list(input()) for _ in range(N + 1)]


    for i in range(N+1):
        for j in range(N):
            if Arr[i][j] == 'A':
                funA(i, j)
            if Arr[i][j] == 'B':
                funB(i, j)
            if Arr[i][j] == 'C':
                funC(i, j)




    cnt = 0
    for i in range(N+1):
        for j in range(N):
            if Arr[i][j] == 'H':
                cnt += 1
    print(f'#{tc} {cnt}')
