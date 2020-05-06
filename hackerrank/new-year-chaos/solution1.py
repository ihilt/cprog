#!/usr/bin/env python3

def minimumBribes(q):
    c = 0
    b = 0
    n = len(q)

    for i in range(n):
        c = 0
        swapped = False
        for j in range(0, n-i-1):
            if q[j] > q[j+1]:
                q[j], q[j+1] = q[j+1], q[j]
                swapped = True
                c += 1
                b += 1
            else:
                c = 0
            if c > 2:
                print("Too chaotic")
                return
        if swapped == False:
            break
    print(b)

if __name__ == '__main__':
    tc = int(input())

    for i in range(tc):
        t = int(input())
        q = list(map(int, input().split()))
        minimumBribes(q)
