import sys
sys.stdin = open("input(p).txt", "r")

TC = 10

for tc in range(1,TC+1):

    ST = []
    N, password = input().split()
    ST.append(password[0])

    for i in range(1, int(N)):
        if not ST:
            ST.append(password[i])
        elif ST[-1] != password[i]:
            ST.append(password[i])
        else:
            ST.pop(-1)

    result = ''
    for i in ST:
        result += i

    print(f'#{tc} {result}')
