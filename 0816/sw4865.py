TC = int(input())

for tc in range(1, TC+1):
    str1 = input()
    str2 = input()

    str1_set = set(str1)

    max_cnt = 0

    for alp1 in str1_set:
        cnt = 0
        for alp2 in str2:
            if alp1 == alp2:
                cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt

    print(f'#{tc} {max_cnt}')




