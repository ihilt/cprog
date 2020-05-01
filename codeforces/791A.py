
if __name__ == '__main__':
    lb = input().split()
    l = int(lb[0])
    b = int(lb[1])

    y = 0
    while y < 10000:
        l *= 3
        b *= 2
        y += 1
        if l > b:
            print(y)
            break
