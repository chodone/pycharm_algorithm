

TC = int(input())

for tc in range(1, TC + 1):
    N, M = map(int, input().split())

    Arr = [[0] * N for _ in range(N)]



    # 가운데 채우기
    dr1 = [0, -1, -1, 0 ]
    dc1 = [0, 0, -1, -1 ]


    for i in range(0, 4, 2):
        Arr[N//2 + dr1[i]][N//2 + dc1[i]] = 2
        Arr[N // 2 + dr1[i+1]][N // 2 + dc1[i+1]] = 1



    dr2 = [0, 1, 1, 1, 0, -1, -1, -1]
    dc2 = [1, 1, 0, -1, -1, -1, 0, 1]

    for i in range(M):
        Y, X, color = map(int, input().split())
        X -= 1
        Y -= 1
        if color == 1:
            a_color = 2
        else:
            a_color = 1

        Arr[X][Y] = color

        for i in range(8):
            if 0 <= X + dr2[i] < N and 0 <= Y + dc2[i] < N:
                check_X = X
                check_Y = Y
                for j in range(1, N):
                    if 0 <= check_X + dr2[i] * j < N and 0 <= check_Y + dc2[i] * j < N:
                        if Arr[check_X + dr2[i] * j][check_Y + dc2[i] * j] == color:
                            for k in range(j):
                                Arr[check_X + dr2[i] * k][check_Y + dc2[i] * k] = color
                            break
                        elif Arr[check_X + dr2[i] * j][check_Y + dc2[i] * j] == 0:
                            break
                    else:
                        break





    black = 0
    white = 0

    for line in Arr:
        for i in line:
            if i == 2:
                white += 1
            elif i == 1:
                black += 1

    print(f'#{tc} {black} {white}')














