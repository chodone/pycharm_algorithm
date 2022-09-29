from collections import deque

def solve():
    Q = []
    cnt = 0
    Q.append((N, 0))
    while Q:
        v,  cnt =Q.pop(0)
        for newV in [v*2, v-20, v+1, v-1 ]:
            if newV == M:
                return cnt + 1
            if 0 < newV <= 1000000 and not visited[newV]:

                Q.append((newV, cnt+1))
                visited[newV] = 1
    return -1


TC = int(input())
for tc in range(1, TC + 1):
    visited = [0] * 1000001
    N, M = map(int, input().split())
    print(f'#{tc} {solve()}')