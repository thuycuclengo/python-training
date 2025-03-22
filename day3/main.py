## - format strings
# I am 23
age = 23

print("I am", age)
print(f"I am {age}") # f - format, fast
template = "I am {}"
print(template.format(age))

## - example - format built in function
name = "John"
age = 30
job = "DEV"

# John is 30 and DEV
print(name + " is " + str(age) + " and " + job)
print(f"{name} is {age} and {job}")
template = "{} is {b} and {c}"
#                            0     1    2
print(template.format(job, b=age, c=name))

## - f-strings
age = 23
print(f"{age*365*24*60*60}")

## comments
"""
print(1)
# print(2) - Ctrl + /
print(3)
"""