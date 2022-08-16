from pprint import pprint
import sys
sys.stdin = open("input.txt", "r")

def palind(mapp):
    N = 100
    M = 100

    while N - M <= 100:
        start = 0
        m = M
        for row in mapp:
            if row[start:m] == row[m-N-1:-N+start-1:-1]:




TC = 10

for tc in range(1, TC+1):
    n = int(input())

    mapp = [input()for _ in range(100)]
    pprint(mapp)
