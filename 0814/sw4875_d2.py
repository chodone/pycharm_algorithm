from pprint import pprint

TC = int(input())

for tc in range(1, TC+1):

    N = int(input())
    map = [list(map(int, input())) for _ in range(N)]

    pprint(map)

    # 시계방향 -  하 우 좌
    dr = [1, 0, 0, -1]
    dc = [0, 1, -1, 0]

    # 경로 stack
    road_stack = []

    #시작점 3 찾기
    cr = 0
    cc = 0
    for column in range(N):
        if cc < map[cr][column]:
            cc = column

    er = 0
    ec = 0



    while not map[er][ec] == 2:

        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                if map[nr][nc] == 0:
                    cr = nr
                    cc = nc
                    if not road_stack[-1][0] + dr[i] and not road_stack[-1][1] + dc[i]:  # 되돌아가
                        road_stack.pop()
                    else:
                        road_stack.append(dr[i], dc[i])

                    break







