# 1. 조합으로 s가 4인 모든 경우의 수를 구한다
# 2. 이 경우의 수를 가지고 BFS를 돌려 인접해 있는지 확인한다
from itertools import combinations
from collections import deque

def yCheck(gComb):
    yNum = 0
    for x, y in gComb:
        if Arr[x][y] == 'Y':
            yNum += 1
        if yNum == 4:
            return False
    return True


def bfs(gComb):
    Visited = [False] * 7
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    Q = deque()
    Q.append(gComb[0])
    Visited[0] = True

    while Q:
        cr, cc = Q.popleft()

        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if (nr, nc) in gComb:
                nextIdx = gComb.index((nr,nc))
                if not Visited[nextIdx]:
                    Q.append((nr, nc))
                    Visited[nextIdx] = True

    if False in Visited:
        return False
    else:
        return True







Arr = [list(input()) for _ in range(5)]
pos = [(i, j) for i in range(5) for j in range(5)]
combs = list(combinations(pos, 7))
res = 0
for comb in combs:
    if yCheck(comb):
        if bfs(comb):
            res += 1

print(res)





