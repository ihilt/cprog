import math

if __name__ == '__main__':
    arr = []

    for i in range(5):
        arr.append(list(map(int, input().split())))

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                break
        if arr[i][j] == 1:
            break
    print(abs(j - 2) + abs(i - 2))
