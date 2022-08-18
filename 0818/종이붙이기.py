
def paper(N):

    if N == 1:
        return 1
    if N == 2:
        return 3

    else:
        return paper(N-1) + 2 * paper(N-2)




TC = int(input())

for tc in range(1, TC+1):
    N = int(input())//10

    print(f'#{tc} {paper(N)}')
