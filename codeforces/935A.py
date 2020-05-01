import math

def cumulative_sum(n):
    return (n - 1)**2 / n

if __name__ == '__main__':
    n = int(input())

    i = 1
    k = 0
    while i < n:
        if n % i == 0:
            k += 1
        i += 1

    print(k)
