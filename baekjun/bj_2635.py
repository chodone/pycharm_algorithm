N = int(input())


maxCnt = 0
lst = []

for i in range(N, 0, -1): # 범위.. 문제에서는 양수일때까지만이라고 했으므로 끝범위는 0, 그리고 두번째 시작값이 N일 수 도 있다

    checkLst = [N , i]

    cnt = 2
    while checkLst[-2] - checkLst[-1] >= 0:  # 0일때도 생각을 해줘야 한다. 문제에서는 음수일 때만이라고 명시
        checkLst.append(checkLst[-2] - checkLst[-1])
        cnt += 1

    if maxCnt <= cnt:
        maxCnt = cnt
        lst = checkLst[::]

print(maxCnt)
print(*lst)







