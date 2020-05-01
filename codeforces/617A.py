if __name__ == '__main__':
    x = int(input())

    n = 0
    n += int(x / 5)
    x %= 5
    n += int(x / 4)
    x %= 4
    n += int(x / 3)
    x %= 3
    n += int(x / 2)
    x %= 2
    n += int(x / 1)

    print(int(n))
