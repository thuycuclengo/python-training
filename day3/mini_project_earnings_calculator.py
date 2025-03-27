name = input("Enter employee's name: ")
hourly_wage = float(input("Employee's hourly wage: $"))
hours_worked = int(input("Hours worked: "))

print(f"{name.strip().title()} earned ${hourly_wage * hours_worked:.2f} this week", end=".\n")
