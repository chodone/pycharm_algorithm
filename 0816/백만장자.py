
TC = int(input())

for tc in range(1, TC+1):

    max_price = 0

    N = int(input())
    price_lst = list(map(int, input().split()))

    margin = 0

    while True:
        max_price = sorted(price_lst)[-1]

        price_lst.index(max_price)

        for price in price_lst[:price_lst.index(max_price)]:
            margin += (max_price - price)

        price_lst = price_lst[price_lst.index(max_price) + 1:]

        if not price_lst:
            break


    print(f'#{tc} {margin}')

