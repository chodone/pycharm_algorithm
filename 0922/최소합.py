def minSum(y, x, sum):
    global res
    sum += arr[y][x]
    if y == N-1 and x == N-1:
        if res > sum:
            res = sum
        return
    elif res < sum:
        return

    # 2방향 탐색 (하, 우)
    dc = [1, 0]
    dr = [0, 1]
    for i in range(2):
        ny, nx = y + dc[i], x + dr[i]
        if ny < N and nx < N:
            minSum(ny, nx, sum)

TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    res = 100000000
    minSum(0, 0, 0)

    print(f'#{tc} {res}')
