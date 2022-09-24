# 1. 1탐색
# 2. delta 순회
# 3. 방문처리 -> while문을 통해서 계속 delta 순회

def bfs(r, c):
    global cnt

    if Arr[r][c] and not Visited[r][c]:
        cnt += 1
        Visited[r][c] = True
        queue = [(r, c)]

        # 우 히 좌 상
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]

        while queue:
            cr, cc = queue.pop(0)

            for i in range(4):
                nr = cr + dr[i]
                nc = cc + dc[i]

                if 0 <= nr < N and 0 <= nc < M and Arr[nr][nc] and not Visited[nr][nc]:
                    Visited[nr][nc] = True
                    queue.append((nr, nc))


    else:
        return






T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split()) # 가로 # 세로 # 배추 수

    Arr = [[0]*M for _ in range(N)]
    Visited = [[False]*M for _ in range(N)]
    cnt = 0

    for i in range(K):
        X, Y = map(int, input().split())
        Arr[Y][X] = 1

    for row in range(N):
        for col in range(M):
            bfs(row, col)

    print(cnt)
