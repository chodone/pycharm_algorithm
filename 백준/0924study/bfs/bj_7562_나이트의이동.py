
def bfs(r, c):

    queue = [(r,c)]


    # 1사분면부터 시계방향
    dr = [-2, -1, 2, 1, 2, 1, -1, -2]
    dc = [1, 2, 2, 1, -1, -2, -2, -1]

    while queue:
        cr, cc = queue.pop(0)

        if cr == goalR and cc == goalC:
            return Arr[cr][cc] - 1

        for i in range(8):
            nr = cr + dr[i]
            nc = cc + dc[i]

            if 0 <= nr < l and 0 <= nc < l and Arr[nr][nc] == 0:

                # 나이트의 이동수를 Arr에 표시하면서 움직이기
                Arr[nr][nc] = Arr[cr][cc] + 1
                queue.append((nr, nc))




T = int(input())

for _ in range(T):
    l = int(input())
    Arr = [[0] * l for _ in range(l)]
    knightR, knightC = map(int, input().split())
    goalR, goalC = map(int, input().split())
    Arr[knightR][knightC] = 1

    print(bfs(knightR, knightC))



