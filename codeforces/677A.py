if __name__ == '__main__':
    nh = input().split()
    n = int(nh[0])
    h = int(nh[1])

    a = list(map(int, input().split()))

    rw = 0
    for i in range(len(a)):
        if a[i] > h:
            rw += 2
        else:
            rw += 1
    print(rw)
