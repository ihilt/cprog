#!/usr/bin/env python3

import math

def bin_dist(x, n, p):
	q = 1 - p
	return (math.factorial(n) / (math.factorial(x) * math.factorial(n - x))) * p**x * q**(n - x)

if __name__ == '__main__':
	result = 0
	for i in range(0, 3):
		result += bin_dist(i, 10, 0.12)
	print(round(result, 3))

	result = 0
	for i in range(2, 11):
		result += bin_dist(i, 10, 0.12)
	print(round(result, 3))