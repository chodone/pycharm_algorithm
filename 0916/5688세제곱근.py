

TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())

    X = N**(1/3)

    if 0 <= round(X) - X <= 0.00001:
        X = round(X)


    if X % 1 == 0:
        X = int(X)
        print(f'#{tc} {X}')

    else:
        print(f'#{tc}', -1)