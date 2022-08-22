TC = 1

for tc in range(1, TC+1):

    prbLen = int(input())
    prb = list(input())

    ST = [prb[1]]
    cal = [prb[0]]

    while ST:
        for i in range(2, prbLen):
            if prb[i] != '+' and prb[i] != '*':
                cal.append(prb[i])
            else:
                if prb[i] == '*':
                    if ST[-1] == '+':
                        ST.append(prb[i])
                    else:
                        while ST[-1] != '+':
                            cal.append(ST[-1])
                            ST.pop()
                        ST.append(prb[i])
                else:
                    while ST:
                        cal.append(ST[-1])
                        ST.pop()

                    ST.append(prb[i])
        if ST:
            for _ in range(len(ST)):
                cal.append(ST[-1])
                ST.pop()




    print(cal)

    ST.append(int(cal[0]))

    while ST:
        for i in range(1, len(cal)):
            if cal[i] != '+' and cal[i] != '*':
                ST.append(int(cal[i]))
            else:










