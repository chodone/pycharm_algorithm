# 찾으면 패턴의 시작 위치를 return
# 못찾으면 -1을 return

def find(t, p):
    M = len(p) # pattern 의 길이
    N = len(t) # 전체 텍스트(target)의 길이

    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1





    return i - M


t = 'a patter matching algorithm test'
p = 'rithmn'

print(find(t,p))

