def dfs(k, start, num):
    if k == 7:
        # num += Arr[start[0]][start[1]]
        if num not in lst:
            lst.append(num)
        return



    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]


    cr, cc = start[0], start[1]

    for i in range(4):
        nr = cr + dr[i]
        nc = cc + dc[i]
        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(k+1, (nr, nc), num + Arr[nr][nc])



TC = int(input())

for tc in range(1, TC + 1):

    Arr = [list(input().split()) for _ in range(4)]
    lst = []


    for i in range(4):
        for j in range(4):
            dfs(1, (i, j), Arr[i][j])
    print(f'#{tc} {len(lst)}')
