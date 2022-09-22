TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())
    lst = []

    for i in range(N):
        lst.append(list(map(int, input().split())))

    lst.sort(key=lambda x:x[1])

    cnt = 1
    start = lst[0][0]
    end = lst[0][1]

    for i in range(1, N):
        if lst[i][0] < end:
            continue
        else:
            start = lst[i][0]
            end = lst[i][1]
            cnt += 1

    print(f'#{tc} {cnt}')