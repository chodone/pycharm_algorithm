def checkCode(line):
    for i in range(M-1, -1, -1):
        res = ''
        if line[i] == 1:
            for j in range(0, 56, 7):
                check=''
                for k in range(7):
                    if line[i-j-k] == 1:
                        check = '1' + check
                    else:
                        check = '0' + check

                res = str(code.index(check)) + res
            return res


TC = int(input())

for tc in range(1, TC + 1):

    N, M = map(int, input().split())

    code = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

    Arr = []
    for i in range(N):
        Arr.append(list(map(int, input())))

    for line in Arr:
        if 1 in line:

            password = checkCode(line)
            break

    checkPassword = 0
    total = 0

    for idx in range(0, 8, 2):
        checkPassword += int(password[idx]) * 3
        checkPassword += int(password[idx+1])
        total += int(password[idx]) + int(password[idx+1])



    if not checkPassword % 10:
        print(f'#{tc} {total}')
    else:
        print(f'#{tc} 0')

