TC = int(input())

for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    res = 0

    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))


    container.sort(reverse=True)
    truck.sort(reverse=True)

    containerCheck = False


    for i in range(M):
        if not container:
            break
        for j in range(len(container)):
            if truck[i] >= container[j]:
                res += container[j]
                container.remove(container[j])
                break

    if res:
        print(f'#{tc} {res}')
    else:
        print(f'#{tc} 0')
