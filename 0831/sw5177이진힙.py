TC = int(input())

for tc in range(1, TC + 1):

    N = int(input())
    Node = [0] * (N+1)
    heap = list(map(int, input().split()))
    parents = [0] * (N+1)

    for i in range(0, N+1, 2):
        parents[i] = i//2
        if i+1 < len(parents):
            parents[i+1] = i//2

    for i in range(N):
        if Node[parents[i+1]] < heap[i]:
            Node[i+1] = heap[i]
        else:
            Node[i+1] = Node[parents[i+1]]
            Node[parents[i+1]] = heap[i]

    sum = 0
    while parents[N]:
        sum += Node[parents[N]]
        N = parents[N]

    print(Node)
    print(parents)
    print(f'#{tc} {sum}')
