TC = int(input())

for tc in range(1, TC+1):
    N = int(input())

    div_lst = [0] * 5
    soinsu = [2, 3, 5, 7, 11]

    for i in range(len(soinsu)):
        if not N % soinsu[i]:
            cnt = 0
            while not N % soinsu[i]:
                N //= soinsu[i]
                cnt += 1
            div_lst[i] = cnt

    print(f'#{tc}', *div_lst)





