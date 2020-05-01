if __name__ == '__main__':
    n = int(input())

    s = 0
    s += int(n / 100)
    n = n - (100 * int(n / 100))
    s += int(n / 20)
    n = n - (20 * int(n / 20))
    s += int(n / 10)
    n = n - (10 * int(n / 10))
    s += int(n / 5)
    n = n - (5 * int(n / 5))
    s += n / 1
    print(int(s))

