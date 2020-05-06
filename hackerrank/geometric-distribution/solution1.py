#!/usr/bin/env python3

import math

def neg_bin_dist(x, n, p):
	q = 1 - p
	m = n - 1
	y = x - 1
	return (math.factorial(m) / (math.factorial(y) * math.factorial(m - y))) * p**x * q**(n - x)

def geo_dist(n, p):
	q = 1 - p
	return q**(n - 1) * p

if __name__ == '__main__':
	result = 0
	for i in range(1, 6):
		result += geo_dist(i, 1 / 3.0)

	print(round(result, 3))

	result = neg_bin_dist(1, 5, 1/3.0)
	print(result)