def merge(st, en):
    if st == en:
        return st
    left = merge(st, (st + en) // 2)
    right = merge((st + en) // 2 + 1, en)
    return winner(left, right)


def winner(a, b):
    if cards[a] == cards[b]:
        return a
    elif cards[a] - cards[b] == 1 or cards[a] - cards[b] == -2:
        return a
    return b


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    cards = list(map(int, input().split()))
    print(f'#{tc} {merge(0, n - 1) + 1}')
