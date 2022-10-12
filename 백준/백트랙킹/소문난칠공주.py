def bfs(k, r, c, s, y):
    global cnt
    if k == 6:
        if s >= 4:
            cnt += 1
        return

    if y == 4:
        return

    # 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]



    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < 5 and 0 <= nc < 5 and not Visited[nr][nc]:
            if Arr[nr][nc] == 'S':
                Visited[nr][nc] = True
                bfs(k+1, nr, nc, s+1, y)
                Visited[nr][nc] = False
            elif Arr[nr][nc] == 'Y':
                Visited[nr][nc] = True
                bfs(k+1, nr, nc, s, y+1)
                Visited[nr][nc] = False








Arr = [list(input())for _ in range(5)]
Visited = [[False]*5 for _ in range(5)]
print(Visited)
sNum = 0
yNum = 0
cnt = 0

for row in range(5):
    for col in range(5):
        if Arr[row][col] == 'S':
            Visited[row][col] = True
            bfs(0, row, col, sNum+1, yNum)
            Visited[row][col] = False


print(cnt)