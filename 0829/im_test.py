import sys
sys.stdin = open('sample_input.txt', 'r')

def divGrade(T1, T2):
    A, B, C = [], [], []
    for i in Score:
        if T1 > i:
            C.append(i)
        elif T1 <= i < T2:
            B.append(i)
        else:
            A.append(i)

    numLst = [len(A), len(B), len(C)]

    for num in numLst:
        if num < K_MIN or num > K_MAX:
            return 1000
    else:
        return max(numLst) - min(numLst)




def divScore():
    T1 = -1
    res = 1000

    for i in range(len(Score)):
        T2 = 0
        if T1 == Score[-1]:
            break
        if T1 < Score[i]:
            T1 = Score[i]
            for j in range(i+1, len(Score)):
                if T2 == Score[-1]:
                    break
                elif T1 < Score[j] and T2 < Score[j]:
                    T2 = Score[j]
                    a = divGrade(T1, T2)
                    if res > a:
                        res = a

    if res == 1000:
        return -1
    else:
        return res







TC = int(input())

for tc in range(1, TC+1):
    N, K_MIN, K_MAX = map(int, input().split())
    Score = list(map(int, input().split()))

    Score.sort() # Score 정렬


    print(f'#{tc} {divScore()}')
