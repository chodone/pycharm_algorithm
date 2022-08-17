# def isEmpty():
#     pass
#
#
#
#
#
# TC = int(input())
#
# for tc in range(1, TC+1):
#     N, M = map(int, input().split())
#     pizza_lst = list(map(int, input().split()))
#     pizza_idx = [idx for idx in range(1, M+1)]
#     fire = [[0, 0] for _ in range(N)]
#
#     while pizza_lst:
#

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    pizza_lst = list(map(int, input().split()))
    oven = list(range(N))  # 화덕에 N개의 피자 인덱 넣기

    while len(oven):
        # 피자 검사
        check = oven.pop(0)
        pizza_lst[check] = pizza_lst[check]//2


        # 치즈가 다 녹은 경우
        if pizza_lst[check] == 0:
            # 더 넣을 피자가 있는지 검사
            if N < M:
                # 있으면 새로운 피자를 넣음
                oven.append(N)
                # 다음에 넣을 피자 인덱스 생성
                N += 1
        # 다 녹지 않은 경우 맨뒤로 다시 넣기
        else:
           oven.append(check)
    print(f'#{tc} {check+1}')







