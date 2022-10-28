from collections import deque


def bfs(r, c):
    Arr[r][c] = 1
    time = 0
    direction = 0
    Q = deque()
    Q.append((r, c))

    cr, cc = 0, 0


    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    while Q:

        nr = cr + dr[direction]
        nc = cc + dc[direction]



        if 0 <= nr < N and 0 <= nc < N:
            if Arr[nr][nc] == 0:

                Arr[nr][nc] = 1
                Q.append((nr, nc))
                tx, ty = Q.popleft()
                Arr[tx][ty] = 0
                    

                time += 1

                if time in accSnakeMove.keys():
                    # 오른쪽 회전
                    if accSnakeMove[time] == 'D':
                        direction = (direction + 1) % 4

                    # 왼쪽 회전
                    elif accSnakeMove[time] == 'L':
                        direction = (direction - 1) % 4

            elif Arr[nr][nc] == 2:


                Arr[nr][nc] = 1
                Q.append((nr, nc))

                time += 1

                if time in accSnakeMove.keys():
                    # 오른쪽 회전
                    if accSnakeMove[time] == 'D':
                        direction = (direction + 1) % 4

                    # 왼쪽 회전
                    elif accSnakeMove[time] == 'L':
                        direction = (direction - 1) % 4
            else:
                return time

        else:
            return time
N = int(input())
Arr = [[0] * N for _ in range(N)]



K = int(input())
for _ in range(K):
    row, col = map(int, input().split())
    Arr[row][col] = 2

L = int(input())
snakeMoveLst = [list(map(str, input().split())) for _ in range(L)]
accSnakeMove = {}
accSec = 0
for i in range(len(snakeMoveLst)):
    accSec += int(snakeMoveLst[i][0])
    accSnakeMove[accSec] = snakeMoveLst[i][1]


a = bfs(0, 0)

print(a)