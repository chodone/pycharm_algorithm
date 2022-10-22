from collections import deque



def find(r, c, d):
    global cnt

    Q = deque()
    Q.append((r,c,d))
    cnt += 1
    Arr[r][c] = 2

    while Q:
        cr, cc, cd = Q.popleft()
        #북 - 서(3) , 남(2), 동(1)
        if cd == 0:
            dr = [0, 1, 0, -1]
            dc = [-1, 0, 1, 0]
            dd = [3, 2, 1, 0]

            for i in range(4):
                nr = cr + dr[i]
                nc = cc + dc[i]
                nd = dd[i]
                if Arr[nr][nc] == 0:
                    Arr[nr][nc] = 2
                    cnt += 1
                    Q.append((nr, nc, nd))
                    break

            else:
                if Arr[cr+1][cc] == 2 or Arr[cr+1][cc] == 0:
                    Q.append((cr+1, cc, cd))
                elif Arr[cr+1][cc] == 1:
                    return




        # 동 - 북(0) 서(3) 남(2)
        elif cd == 1:
            dr = [-1, 0, 1, 0]
            dc = [0, -1, 0, 1]
            dd = [0, 3, 2, 1]

            for i in range(4):
                nr = cr + dr[i]
                nc = cc + dc[i]
                nd = dd[i]
                if Arr[nr][nc] == 0:
                    Arr[nr][nc] = 2
                    cnt += 1
                    Q.append((nr, nc, nd))
                    break

            else:
                if Arr[cr][cc-1] == 2 or Arr[cr][cc-1] == 0:
                    Q.append((cr, cc-1, cd))
                elif Arr[cr][cc-1] == 1:
                    return

        #남 - 동(1) 북(0) 서(3)
        elif cd == 2:
            dr = [0, -1, 0, 1]
            dc = [1, 0, -1, 0]
            dd = [1, 0, 3, 2]

            for i in range(4):
                nr = cr + dr[i]
                nc = cc + dc[i]
                nd = dd[i]
                if Arr[nr][nc] == 0:
                    Arr[nr][nc] = 2
                    cnt += 1
                    Q.append((nr, nc, nd))
                    break

            else:
                if Arr[cr-1][cc] == 2 or Arr[cr-1][cc] == 0:
                    Q.append((cr-1, cc, cd))
                elif Arr[cr-1][cc] == 1:
                    return

        #서 - 남(2) 동(1) 북(0)
        elif cd == 3:
            dr = [1, 0, -1, 0]
            dc = [0, 1, 0, -1]
            dd = [2, 1, 0, 3]

            for i in range(4):
                nr = cr + dr[i]
                nc = cc + dc[i]
                nd = dd[i]
                if Arr[nr][nc] == 0:
                    Arr[nr][nc] = 2
                    cnt += 1
                    Q.append((nr, nc, nd))
                    break

            else:
                if Arr[cr][cc+1] == 2 or Arr[cr][cc+1] == 0:
                    Q.append((cr, cc+1, cd))
                elif Arr[cr][cc+1] == 1:
                    return




N, M = map(int, input().split())
r, c, d = map(int, input().split())

Arr = [list(map(int, input().split()))for _ in range(N)]
cnt = 0
find(r,c,d)

print(cnt)
