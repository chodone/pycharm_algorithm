
TC = int(input())

for tc in range(1, TC+1):
    og_memory = list(map(int, input()))

    memory = [0] * len(og_memory)
    v = 0
    cnt = 0

    while memory != og_memory:
        if v == 0:
            for i in range(len(og_memory)):
                if og_memory[i] == 1:
                    memory[i] = 1

            v = 1
            cnt += 1
        else:
            for i in range(len(og_memory)):
                if og_memory[i] == 0:
                    memory[i] = 0

            v = 0
            cnt += 1


    print(memory, cnt)







