## join collections of strings
house_types = ["penthouse", "villa", "apartment"]

print(f"Our company provides these house types: {', '.join(house_types)}.")

house_types = ', '.join(house_types)
print(f"Our company provides these house types: {house_types}.")  # penthouse, villa, apartment

## we can only join collections of strings -> convert a list of numbers to a string first
numbers = [9, 58, 544, -1, 0]
stringified_numbers = []

for number in numbers:
	stringified_numbers.append(str(number))
print(' '.join(stringified_numbers))
