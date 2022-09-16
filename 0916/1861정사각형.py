
TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())


    visited = [[False] * N for _ in range(N)]

    Arr =[]
    for i in range(N):
        Arr.append(list(map(int, input().split())))

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    col, row = 0, 0

    maxRoom = 1

    while col < N and row < N:
        room = 1
        for i in range(4):
            newC = col + dc[i]
            newR = row + dr[i]

            if Arr[newC][newR] == Arr[col][row] + 1:



