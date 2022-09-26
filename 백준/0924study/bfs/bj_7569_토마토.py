from pprint import pprint
# 나는야 멋쟁이 토마토~ 토마토!!
# 재귀 형테로 풀어야 가능할듯??
# day를 어디에서 증가시켜줄 것인가?

def bfs(lst, day):

    if not lst:

        return day


    while lst:

        # 1층위 1층아래 우 하 좌 상
        dh = [-1, 1, 0, 0, 0, 0]
        dr = [0, 0, 0, 1, 0, -1]
        dc = [0, 0, 1, 0, -1, 0]


        queue = [lst.pop(0)]

        while queue:
            ch, cr, cc = queue.pop(0)
            newLst = []


            for i in range(6):
                nh = ch + dh[i]
                nr = cr + dr[i]
                nc = cc + dc[i]

                if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and not Arr[nh][nr][nc]:
                    newLst.append((nh, nr, nc))
                    Arr[nh][nr][nc] = 1

        bfs(newLst, day + 1)









M, N, H = map(int , input().split())

# 3중 배열 선언
Arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
Visitied = [[[False] * M for _ in range(N)] for _ in range(H)]
startLst = []
day = 0

for height in range(H):
    for row in range(N):
        for col in range(M):
            if Arr[height][row][col] == 1:
                startLst.append((height, row, col))

a = bfs(startLst, day)


pprint(Arr)
print(a)



