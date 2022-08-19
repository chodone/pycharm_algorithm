# TC = int(input())
#
# for tc in range(1, TC+1):
#     N = int(input())
#
#     mapp = [list(map(int, input().split())) for _ in range(N)]
#
#

def count(idx, visited, SUM):
    global MIN
    if idx >= N:
        if SUM < MIN:
            MIN = SUM
        return
    # 가치치기
    if SUM > MIN:
        return

    for k in range(0, N):
        if visited[k] == 0:  # k번째 값에 접근한적이 없다면
            SUM += mapp[idx][k]

            visited[k] = 1

            count(idx + 1, visited, SUM)

            visited[k] = 0  # 원상복구
            SUM -= mapp[idx][k]


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    mapp = [list(map(int, input().split()) for _ in range(N))]

    visited = {}

    for i in range(0, N):
        visited[i] = 0

    SUM = 0
    MIN = 99999

    count(0, visited, SUM)

    print(f'#{tc} {MIN}')