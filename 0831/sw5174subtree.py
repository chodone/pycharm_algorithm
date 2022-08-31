def preorder(root):

    if root != 0:

        preorder(tree[root][0])
        preorder(tree[root][1])
        global cnt
        cnt += 1
    return cnt



TC = int(input())

for tc in range(1, TC+1):
    # 간선의 수 - E , 목표 노드 N
    E, N = map(int, input().split())

    tree = [[0, 0] for _ in range(E + 2)]
    lst = list(map(int, input().split()))
    cnt = 0

    for i in range(E):
        p, c = lst[2*i], lst[2*i + 1]
        if tree[p][0] == 0:
            tree[p][0] = c
        else:
            tree[p][1] = c


    print(f'#{tc} {preorder(N)}')







