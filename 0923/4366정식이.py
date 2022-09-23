# 이진수의 i번째가 틀린 경우

def check():
    # 이진수의 i번째가 틀린 경우
    for i in range(N):
        #삼진수의 j번째가 틀린경우
        for j in range(M):
            b = 이진수의 i번째 데이터를 변경하고 0 <->
                b[i] = (b[i]+1) % 2
            t = 삼진수의 i번째 데이터를 변경해서 0 : 1,2, 1:2,
                for k in [1,2]:
                    t[j] = (t[j] + k) % 3
                    if b의 십진수 == t 의 십진수:
                        return b의 십진수
    return -1
