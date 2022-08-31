def inorder(root):
    if root != 0:

        inorder(tree[root][0])
        res.append(root)
        inorder(tree[root][1])


TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())

    tree = [[0,0] for _ in range(N + 1)]
    node = list(i for i in range(2, N+1))

    res = []

    for i in range(1, N+1):

        tree[i][0] = node.pop(0)
        if not node:
            break

        tree[i][1] = node.pop(0)

        if not node:
            break

    inorder(1)
    print(res)
    print(f'#{tc} {res.index(1) +1} {res.index(N//2) + 1}')



# 아이디어 정리
# 연결노드 리스트를 만들고 중위순위를 돌려 노드 인덱스  리스트를 만든다
# [1, 2, 3, 4, 5, 6, 7, 8]
# [8, 4, 2, 5, 1, 6, 3, 7]

# 뿌리는 항상 1의 인덱스+1, N//2 인덱스 + 1


