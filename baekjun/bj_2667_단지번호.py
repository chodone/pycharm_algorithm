def find(r, c):

    global cnt

    # 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    Arr[r][c] = 0
    cnt += 1

    Q = [(r, c)]

    while Q:
        cr, cc = Q.pop(0)

        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]

            if 0 <= nr < N and 0 <= nc < N and Arr[nr][nc] == 1:
                Arr[nr][nc] = 0
                cnt += 1
                Q.append((nr, nc))

    lst.append(cnt)
    cnt = 0









N = int(input())
Arr = [list(map(int, input())) for _ in range(N)]
cnt = 0
lst = []

for row in range(N):
    for col in range(N):
        if Arr[row][col] == 1:
            find(row, col)

lst.sort()

print(len(lst))
for i in lst:
    print(i)