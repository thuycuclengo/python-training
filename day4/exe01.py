movies = [("Squid Game", "Steve Jobs", 2024, 1000)]
title = input("Your favorite movie: ")
director = input("Director's name: ")
release_year = int(input("Release year: "))
budget = int(input("Budget: "))
new_movie = (title, director, release_year, budget)

print(f"{new_movie[0]} {new_movie[2]}")
movies.append(new_movie)

print(movies)
# del movies[0]
# movies.remove(movies[0])
movies.pop(0)

print(movies)
