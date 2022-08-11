import sys
sys.stdin = open("input.txt", "r")


TC = 10

for tc in range(1, TC+1):

    N = int(input())

    curR = 99
    curC = 0

    ladder = [list(map(int, input().split())) for _ in range(100)]

    dr = [0, 0, -1]    # 좌 우 상
    dc = [-1, 1, 0]

    for col in range(100):
        if ladder[99][col] == 2:
            curC = col

    while curR > 0:
        for i in range(3):
            newR = curR + dr[i]
            newC = curC + dc[i]

            if 0<=newR <100 and 0<=newC <100:
                if ladder[newR][newC] == 1:
                    ladder[curR][curC] = 0
                    curR, curC = newR, newC
                    break


    print(f'#{tc} {curC}')







