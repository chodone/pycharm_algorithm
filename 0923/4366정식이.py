
def check():
    for i in range(len(binary)):
        binary[i] = str((int(binary[i]) + 1) % 2)
        bDec = int(int(binary), 2)
        for j in range(len(triad)):
            for k in [1,2]:
                triad[j] = str((int(triad[j]) + k) % 3)
                tDec = int(int(triad), 3)

                if tDec == bDec:
                    return bDec

    return -1


TC = int(input())

for tc in range(1, TC + 1):
        binary = list(input())
        triad = list(input())

        a = check()
        print(a)

