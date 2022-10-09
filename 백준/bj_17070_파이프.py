import sys

def bfs(r, c, flag):
    global cnt
    dr = [0, 1, 1]
    dc = [1, 1, 0]

    if r == N-1 and c == N-1:
        cnt += 1

        return



    if flag == 0:
        for i in range(2):
            if i == 0:
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < N and not Arr[nr][nc]:
                    bfs(nr, nc, 0)
            if i == 1:
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < N and not Arr[nr][nc] and not Arr[nr-1][nc] and not Arr[nr][nc-1]:
                    bfs(nr, nc, 1)


    if flag == 2:
        for i in range(2,0,-1):
            if i == 2:
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < N and not Arr[nr][nc]:
                    bfs(nr, nc, 2)
            if i == 1:
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < N and not Arr[nr][nc] and not Arr[nr-1][nc] and not Arr[nr][nc-1]:
                    bfs( nr, nc, 1)

    if flag == 1:
        for i in range(3):
            if i == 0:
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < N and not Arr[nr][nc]:
                    bfs(nr, nc, 0)
            if i == 1:
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < N and not Arr[nr][nc] and not Arr[nr-1][nc] and not Arr[nr][nc-1]:
                    bfs(nr, nc, 1)
            if i == 2:
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < N and not Arr[nr][nc]:
                    bfs(nr, nc, 2)








N = int(input())
Arr = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]
cnt = 0
minV = 1e10

bfs(0,1,0)

print(cnt)

