for i in range(1, 16):
	# if i % 15 == 0:
	# 	print("Fizz Buzz")
	# elif i % 3 == 0:
	# 	print("Fizz")
	# elif i % 5 == 0:
	# 	print("Buzz")
	# else:
	# 	print(i)

	flag = (i % 3 == 0) * 'Fizz' + (i % 5 == 0) * 'Buzz'
	print(flag or i)
