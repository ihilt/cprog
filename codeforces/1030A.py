if __name__ == '__main__':
	n = input().split()
	a = map(int, input().split())

	if sum(a) > 0:
		print("HARD")
	else:
		print("EASY")