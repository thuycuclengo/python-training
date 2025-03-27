## Lists (mutable)
places = ["Sapa", "Phan Thiet", "Ha Noi", "Sai Gon"]
print(places)

##
print(["Sapa", "Phan Thiet", "Ha Noi", "Sai Gon"])

## index
showtime = [20.00, 13.40, 08.35, 19.20]
# add item at the end of list
showtime.append(23.15)
print(showtime)
# index count from end
print(showtime[-3])

## add an item in the middle
month = ["Jan", 1, "Feb", 2, "June", 6, "Dec", 12]

# month.insert(position, object insert)
month.insert(4, "Mar")
print(month)

month.insert(5, 3)
print(month)

month.insert(12, 9999)
print(month)

## remove an item
personality = ["rude", 1, "hilarious", 2, "introvert", 3]

# .pop: remove last item
personality.pop()
print(personality)

personality.remove("hilarious")
print(personality)

del personality[3]
print(personality)

# print removed item
last_in_line = personality.pop(1)
print(last_in_line)

personality.clear()
print(personality)

## Tuples (immutable)
coffee = [
    ("Americano", 45 * 1000, "VND"),
    ("Flat white", 45 * 1000, "VND"),
    ("Cold brew", 55 * 1000, "VND")
]
print(coffee)
print("--->", coffee[1])

# access an index in a tuple
# variable_name[tuple_order][index_in_tuple]
print(coffee[0][1])

## - tuple
a = [1,]
print(a)
