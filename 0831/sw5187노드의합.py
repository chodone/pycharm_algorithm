def cal(root):
    Node[root] = Node[Tree[root][0]] + Node[Tree[root][1]]


def postOrder(root):
    if root != 0:
        postOrder(Tree[root][0])
        postOrder(Tree[root][1])
        if not Node[root]:
            cal(root)



TC = int(input())

for tc in range(1, TC + 1):
    N, M, L = map(int, input().split())

    Node = [0] * (N+1)
    Tree = [[0, 0] for _ in range(N+1)]

    # Tree 채우기
    for i in range(1, N//2 + 1):
        Tree[i][0] = 2*i
        if 2*i < N:
            Tree[i][1] = 2*i + 1


    for i in range(M):
        nodeNum, value = map(int, input().split())
        Node[nodeNum] = value

    postOrder(1)
    print(f'#{tc} {Node[L]}')
