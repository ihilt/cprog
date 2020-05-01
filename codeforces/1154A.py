if __name__ == '__main__':
    nums = input().split()
    nums = list(map(int, nums))

    x1 = nums[0]
    x2 = nums[1]
    x3 = nums[2]
    x4 = nums[3]

    s = (x1 + x2 + x3 + x4) / 3

    if s == x1:
        print(int(s - x2), end = " ")
        print(int(s - x3), end = " ")
        print(int(s - x4), end = " ")
    elif s == x2:
        print(int(s - x1), end = " ")
        print(int(s - x3), end = " ")
        print(int(s - x4), end = " ")
    elif s == x3:
        print(int(s - x1), end = " ")
        print(int(s - x2), end = " ")
        print(int(s - x4), end = " ")
    elif s == x4:
        print(int(s - x1), end = " ")
        print(int(s - x2), end = " ")
        print(int(s - x3), end = " ")
