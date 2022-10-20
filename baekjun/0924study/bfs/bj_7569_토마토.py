from pprint import pprint
# 나는야 멋쟁이 토마토~ 토마토!!
# 재귀 형테로 풀어야 가능할듯??
# day를 어디에서 증가시켜줄 것인가?

def bfs(lst, day):
    global totalDay
    newLst = []

    if not lst:
        totalDay = day - 1
        return


    while lst:

        # 1층위 1층아래 우 하 좌 상
        dh = [-1, 1, 0, 0, 0, 0]
        dr = [0, 0, 0, 1, 0, -1]
        dc = [0, 0, 1, 0, -1, 0]


        ch, cr, cc = lst.pop(0)
        for i in range(6):
            nh = ch + dh[i]
            nr = cr + dr[i]
            nc = cc + dc[i]

            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and not Arr[nh][nr][nc]:
                newLst.append((nh, nr, nc))
                Arr[nh][nr][nc] = 1

    bfs(newLst, day+1)


def checkTomato():
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if not Arr[h][r][c]:
                    return False
    return True





M, N, H = map(int , input().split())

# 3중 배열 선언
Arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
startLst = []
totalDay = 0

check1 = checkTomato()

if check1:
    print(0)
else:
    for height in range(H):
        for row in range(N):
            for col in range(M):
                if Arr[height][row][col] == 1:
                    startLst.append((height, row, col))

    bfs(startLst, 0)
    check2 = checkTomato()
    if check2:
        print(totalDay)
    else:
        print(-1)



