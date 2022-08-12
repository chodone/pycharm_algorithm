def prime_lst(A, n):
    sieve = [True] * (n+1)
    sieve[0] = False
    sieve[1] = False

    m = int(n ** 0.5)
    for i in range(2 , m+1):
        if sieve[i] == True:
            for j in range(i+i, n + 1, i):
                sieve[j] = False

    return [i for i in range(A,n+1) if sieve[i] == True]



TC = int(input())

for tc in range(1, TC+1):
    D, A, B = map(int, input().split())
    spePrime_lst = []

    # 소수 구하기
    a = prime_lst(A, B)




    # 특별한 소수 구하기
    for i in a:
        for j in str(i):
            if int(j) == D:
                spePrime_lst.append(i)
                break

    print(f'#{tc} {len(spePrime_lst)}')



