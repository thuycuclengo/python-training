a = [2022, 2017]
b = a.copy()
print(id(a), id(b))

print(a == b)
print(a is b)

##
numbers = [1, 2, 3, 4]
print(id(numbers))

new_numbers = numbers + [5]
numbers += [5]
print(numbers)
print(id(numbers))

print(new_numbers)

print(id(numbers), id(new_numbers))

print(numbers == new_numbers)
print(numbers is new_numbers)

##
numbers = [1, 2, 3, 4]
print(id(numbers))
numbers.append(5)
print(id(numbers))

##
n = int(input("Give a number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

##
hours_worked = int(input("Hours worked: "))
hourly_wage = float(input("Hourly wage: $"))

amount = hourly_wage * hours_worked

if hours_worked > 40:
    amount = 40 * hourly_wage + (hours_worked - 40) * 1.1 * hourly_wage
print(f"${amount:.2f}")
