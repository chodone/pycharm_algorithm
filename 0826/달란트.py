TC = int(input())

for tc in range(1, TC + 1):
    X, Y = map(int, input().split())
    res = (X // Y)**(Y - X%Y) * (X//Y+1)**(X%Y)

    print(f'#{tc} {res}')