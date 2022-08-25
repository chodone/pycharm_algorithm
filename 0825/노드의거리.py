def bfs(st, ed):

    dist = [0] * (V+1)

    queue = [st]


    while queue:
        cn = queue.pop(0)


        for point in nodeLine:
            if point[0] == cn:
                if not dist[point[1]]:
                    dist[point[1]] = dist[cn] + 1
                    queue.append(point[1])
                if point[1] == ed:
                    return dist[cn] + 1
            elif point[1] == cn:
                if not dist[point[0]]:
                    dist[point[0]] = dist[cn] + 1
                    queue.append(point[0])
                if point[0] == ed:
                    return dist[cn] + 1
    return 0







TC = int(input())

for tc in range(1, TC + 1):
    V, E = map(int, input().split())

    nodeLine = [list(map(int, input().split())) for i in range(E)]

    st, ed = map(int, input().split())

    print(f'#{tc} {bfs(st, ed)}')
