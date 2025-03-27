employees = [
	("Rolf Smith", 35, 8.75),
	("Anne Pun", 30, 12.50),
	("Charlie Lee", 50, 15.50),
	("Bob Smith", 20, 7.00)
]

total = count = 0
for employee in employees:
	print(f"{employee[0]} earned {employee[1] * employee[2]}")
	total += employee[-1]
	count += 1

average = total / count
print(average)

for employee in employees:
	if employee[-1] > average:
		print(employee[0])
