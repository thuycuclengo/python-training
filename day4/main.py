##
places = ["Sapa", "Phan Thiet", "Ha Noi", "Sai Gon"]
print(places)

##
print(["Sapa", "Phan Thiet", "Ha Noi", "Sai Gon"])

## index
movie_time = [20.00, 13.40, 08.35, 19.20]
movie_time.append(23.15)
print(movie_time[-3])

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

last_in_line = personality.pop(1)
print(last_in_line)

personality.clear()
print(personality)

## Tuples
