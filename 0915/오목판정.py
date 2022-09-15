def diag1(row,col):
    for i in range(4):
        col -= 1
        row += 1
        if 0 <= col < N and 0 <= row < N:
            if Arr[row][col] == '.':
                return False

        else:
            return False

    return True

def diag2(row,col):
    for i in range(4):
        col += 1
        row += 1
        if 0 <= col < N and 0 <= row < N:
            if Arr[row][col] == '.':
                return False

        else:
            return False

    return True


def trans(row,col):
    for i in range(4):
        col += 1
        if 0 <= col < N:
            if Arr[row][col] == '.':
                return False

        else:
            return False

    return True

def length(row,col):
    for i in range(4):
        row += 1
        if 0 <= row < N:
            if Arr[row][col] == '.':
                return False

        else:
            return False

    return True





TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())

    Arr = [list(input())for _ in range(N)]
    forExit = True

    for row in range(N):
        if forExit:
            for col in range(N):
                if Arr[row][col] == 'o':
                    if length(row,col):
                        print(f'#{tc} YES')
                        forExit = False
                        break
                    if trans(row,col):
                        print(f'#{tc} YES')
                        forExit = False
                        break
                    if diag1(row,col):
                        print(f'#{tc} YES')
                        forExit = False
                        break
                    if diag2(row,col):
                        print(f'#{tc} YES')
                        forExit = False
                        break
        else:
            break
    else:
        print(f'#{tc} NO')


