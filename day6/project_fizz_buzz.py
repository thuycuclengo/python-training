for i in range(1, 16):
	if i % 3 == 0:
		print("Fizz")
	elif i % 5 == 0:
		print("Buzz")
	elif i % 3 == 0 and i % 5 == 0:
		print("Fizz Buzz")
	else:
		print(i)
