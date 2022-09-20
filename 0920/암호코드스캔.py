import sys
sys.stdin = open('input.txt')

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
    N, M = map(int, input().split())

    Arr = [list(input().strip()) for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if Arr[i][j] == '0':
                Arr[i][j] = Arr[i][j]*4
            else:
                Arr[i][j] = decToBin(hexToDec(Arr[i][j]))

        Arr[i] = (''.join(Arr[i]))


    res = 0

    for row in range(1, N):
        j = M * 4 - 1  # 오른쪽 끝
        # 제일 오른쪽 끝에 있는 1을 찾는다
        while j >= 56:
            if Arr[row][j] == '1' and Arr[row - 1][j] == '0':
                code = [0, 0, 0, 0, 0, 0, 0, 0]

                for i in range(8):
                    a = [0, 0, 0]
                    # a[2]=1의 갯수를 세고
                    while Arr[row][j] == '1':
                        a[2] += 1
                        j -= 1
                    # a[1]=0의 갯수를 세고
                    while Arr[row][j] == '0':
                        a[1] += 1
                        j -= 1

                    # a[0]=1의 갯수를 세고
                    while Arr[row][j] == '1':
                        a[0] += 1
                        j -= 1

                    while Arr[row][j] == '0':
                        j -= 1

                    k = min(a)

                    code_pat = {'211':0, '221':1, '122':2, '411':3, '132':4, '231':5, '114':6, '312':7, '213':8, '112':9}

                    code[7-i] = code_pat[str(a[0]//k * 100 + a[1]//k * 10 + a[2]//k)]

                checkPassword = 0
                total = 0

                for idx in range(0, 8, 2):
                    checkPassword += int(code[idx]) * 3
                    checkPassword += int(code[idx + 1])
                    total += int(code[idx]) + int(code[idx + 1])
                if not checkPassword % 10:
                    res += total



            else:
                j -= 1
    print(f'#{tc} {res}')




