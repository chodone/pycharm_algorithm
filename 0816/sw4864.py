TC = int(input())

for tc in range(1, TC+1):
    str1 = input()
    str2 = input()

    N = len(str1)
    M = len(str2)

    for idx in range(M):
        if str1 == str2[idx:idx+N]:
            print(f'#{tc} 1')
            break
    else:
        print(f'#{tc} 0')




