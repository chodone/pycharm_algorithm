# 16진수 -> 10진수
def hexToDec(n):
    if ord('0') <= ord(n) <= ord('9'):
        return ord(n) - ord('0')
    return ord(n) - ord('A') + 10


# 10진수 -> 2진수
def decToBin(n):
    res = ''
    # 2의 지수로 나누기
    for index in range(3, -1, -1):
        res += str(n // (2**index))
        n %= (2**index)
    return res


TC = int(input())

for tc in range(1, TC + 1):
    N, lst = input().split()
    N = int(N)

    result = ''
    for num in lst:
        result += decToBin(hexToDec(num))

    print(f'#{tc} {result}')