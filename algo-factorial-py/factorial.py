def factorial(num):
	if(num == 1 or num == 0):
		return num
	return num * factorial(num - 1)