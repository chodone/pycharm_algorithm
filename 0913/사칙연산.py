def cal(b):
    if Node[b] == '+':
        Node[b] = Node[Tree[b][0]] + Node[Tree[b][1]]
    elif Node[b] == '-':
        Node[b] = Node[Tree[b][0]] - Node[Tree[b][1]]
    elif Node[b] == '*':
        Node[b] = Node[Tree[b][0]] * Node[Tree[b][1]]
    elif Node[b] == '/':
        Node[b] = Node[Tree[b][0]] // Node[Tree[b][1]]




def inOrder(root):
    if root != 0:
        inOrder(Tree[root][0])
        inOrder(Tree[root][1])
        cal(root)






TC = 10

for tc in range(1, TC+1):
    N = int(input())
    Node = [0] * (N+1)
    Tree = [[0,0] for _ in range(N+1)]
    Parent = [0] * (N + 1)
    res = 0

    for i in range(N):
        lst = list(input().split())
        if lst[1] == '+' or lst[1] == '-' or lst[1] =='*' or lst[1] =='/':
            Node[int(lst[0])] = lst[1]
            Tree[int(lst[0])][0] = int(lst[2])
            Tree[int(lst[0])][1] = int(lst[3])
            Parent[int(lst[2])] = int(lst[0])
            Parent[int(lst[3])] = int(lst[0])

        else:
            Node[int(lst[0])] = int(lst[1])


    inOrder(1)

    print(f'#{tc} {Node[1]}')
