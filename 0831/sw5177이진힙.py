# TC = int(input())
#
# for tc in range(1, TC + 1):
#
#     N = int(input())
#     Node = [0] * (N+1)
#     heap = list(map(int, input().split()))
#     parents = [0] * (N+1)
#
#     for i in range(0, N+1, 2):
#         parents[i] = i//2
#         if i+1 < len(parents):
#             parents[i+1] = i//2
#
#
#     for i in range(N):
#         if Node[parents[i+1]] < heap[i]:
#             Node[i+1] = heap[i]
#         else:
#             Node[i+1] = Node[parents[i+1]]
#             Node[parents[i+1]] = heap[i]
#
#     sum = 0
#     while parents[N]:
#         sum += Node[parents[N]]
#         N = parents[N]
#
#     print(Node)
#     print(parents)
#     print(f'#{tc} {sum}')



TC = int(input())

for tc in range(1, TC + 1):
    n = int(input())  # 목표 노드
    node = [0] + list(map(int, input().split()))


    # 위치 바꾸기
    for i in range(1, n + 1):
        while node[i // 2] > node[i]:  # 부모가 나보다 클때 바꿔주기
            node[i // 2], node[i] = node[i], node[i // 2]
            i //= 2  # 다음 조상도 검토

    # 조상 노드  더하기

    res = 0
    p = n // 2
    while p > 0:
        res += node[p]
        p //= 2

    print(f'#{tc} {res}')
    print(node)
