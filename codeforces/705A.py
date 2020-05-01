if __name__ == '__main__':
    n = int(input())

    i = 0
    while i < 101 and i < n:
        if n == 1:
            print("I hate", end = " ")
            break
        if i % 2 == 0:
            print("I hate", end = " ")
        else:
            print("I love", end = " ")
        i += 1
        if i < n:
            print("that", end = " ")
    print("it")
