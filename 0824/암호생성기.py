def cycle(queue):
    for i in range(1,6):
        a = queue.pop(0)
        a -= i
        if a >= 0:
            queue.append(a)
        else:
            queue.append(0)

        if a <= 0:
            return



TC = 10

for tc in range(1, TC + 1):
    N = int(input())
    queue = [0] * 8

    lst = list(map(int, input().split()))

    for i in range(8):
        queue[i] = lst[i]

    while queue[-1]:
        cycle(queue)

    print(f'#{tc}', *queue)




