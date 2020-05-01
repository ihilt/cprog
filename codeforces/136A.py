if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    f =[]

    while n > 0:
        f.append(0)
        n -= 1
    for i in range(len(arr)):
        f[arr[i]-1] = i+1

    for i in range(len(f)):
        print(f[i], end = " ")
