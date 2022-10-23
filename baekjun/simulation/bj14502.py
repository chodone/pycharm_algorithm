# 연구소

# 아이디어 정리
# 3개 조합을 구한 후 -> bfs 재귀
# 재귀 종료 조건 - 2가 더이상 퍼지지 못할때 종료
# 안전영역의 최대값 -> 바이러스의 최소값
# 백트래킹 -> 바이러스의 수가 minV을 넘어갈 시 return
from collections import deque
import copy


def bfs(vl):
    global minV, res
    virusCnt = 0
    safeCnt = 0
    tArr = copy.deepcopy(Arr)
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    Q = deque()
    for virus in vl:
        Q.append(virus)
        virusCnt += 1

    while Q:
        cr, cc = Q.popleft()

        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not tArr[nr][nc]:
                tArr[nr][nc] = 2
                virusCnt += 1
                if virusCnt >= minV:
                    return
                Q.append((nr, nc))

    minV = virusCnt
    for row in range(N):
        for col in range(M):
            if not tArr[row][col]:
                safeCnt += 1

    res = safeCnt





def comb(k):
    if k == 2:
        virusLst = []

        for row in range(N):
            for col in range(M):
                if Arr[row][col] == 2:
                    virusLst.append((row,col))

        bfs(virusLst)

        return


    for comR in range(N):
        for comC in range(M):
            if not Visited[comR][comC] and not Arr[comR][comC]:
                Arr[comR][comC] = 1
                comb(k+1)
                Arr[comR][comC] = 0





N, M = map(int, input().split())
Arr = [list(map(int, input().split())) for _ in range(N)]


# 초기 Visited 세팅
Visited = [[False] * M for _ in range(N)]
# for vr in range(N):
#     for vc in range(M):
#         if Arr[vr][vc] == 1 or Arr[vr][vc] == 2:
#             Visited[vr][vc] = True
minV = 1e10
res = 0

for row in range(N):
    for col in range(M):
        if Arr[row][col] == 0:
            Visited[row][col] = True
            Arr[row][col] = 1
            comb(0)
            Arr[row][col] = 0



print(res)
