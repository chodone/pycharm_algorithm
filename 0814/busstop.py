# 모든 정류장은 1-1000까지 번호 부여
# 모든 버스는 출발인 A와 도착B는 반드시 정차
# 일반 버스는 모든역 정차
# 급행 버스는 A가 짝수이면 짝수역, A가 홀수이면 홀수역 정차
# 굉역 급행 버스는 A가 짝수 - 4의 배수 , A가 홀수 - 3의 배수이면수 10의 배수는 아닌역 정차
# 버스 종류, A ,B 순으로 주어진다.
# 최대 몇개의 노선이 같은 정류장에서 정차하는지 알아보자






TC = int(input())

for tc in range(1, TC+1):
    busStop = [0] * 1001
    N = int(input())

    for i in range(N):
        bus_type, A, B = map(int, input().split())

        busStop[B] += 1

        if bus_type == 1:
            for i in range(A, B):
                busStop[i] += 1

        elif bus_type == 2:
            if not A % 2:
                for i in range(A, B):
                    if not i%2:
                        busStop[i] += 1
            else:
                for i in range(A, B):
                    if i%2:
                        busStop[i] += 1

        else:
            if not A % 2:
                if A % 4:
                    for i in range(A,B):
                        if not i % 4:
                            busStop[i] += 1

                else:
                    busStop[A] += 1
                    for i in range(A,B):
                        if not i % 4:
                            busStop[i] += 1
            else:
                if A % 3:
                    busStop[A] += 1
                    for i in range(A,B):
                        if not i % 3 and i % 10:
                            busStop[i] += 1
                else:
                    for i in range(A,B):
                        if not i % 3 and i % 10:
                            busStop[i] += 1

    result = busStop[0]
    for i in busStop[1:]:
        if i > result:
            result = i

    print(f'#{tc} {result}')
















