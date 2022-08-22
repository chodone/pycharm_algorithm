

def countingSort(data):

    counts = [0] * 10000
    result = [0] * len(data)


    for i in range(0, len(data)):
        counts[data[i]] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i-1]

    for i in range(len(data)-1, -1, -1):
        counts[data[i]] -= 1
        result[counts[data[i]]] = data[i]

    return result



TC = int(input())



for tc in range(1, TC+1):

    max_price = 0

    N = int(input())
    price_lst = list(map(int, input().split()))

    margin = 0

    while True:
        max_price = countingSort(price_lst)[-1]

        price_lst.index(max_price)

        for price in price_lst[:price_lst.index(max_price)]:
            margin += (max_price - price)

        price_lst = price_lst[price_lst.index(max_price) + 1:]

        if not price_lst:
            break


    print(f'#{tc} {margin}')

