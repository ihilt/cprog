import math

def poisson_distribution(l, k):
	return l**k * math.e**(-l) / math.factorial(k)

if __name__ == '__main__':
	result = 0
	# for i in range(0, 4):
	result += poisson_distribution(2.5, 5)
	print(round(result, 3))