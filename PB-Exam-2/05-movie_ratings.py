import sys
from sys import maxsize

film_num = int(input())
max_rating = -sys.maxsize
min_rating = sys.maxsize

highest_rated_film = None
lowest_rated_film = None

total_rating = 0

for _ in range(film_num):
    film_name = input()
    film_rating = float(input())

    if film_rating > max_rating:
        max_rating = film_rating
        highest_rated_film = film_name

    if film_rating < min_rating:
        min_rating = film_rating
        lowest_rated_film = film_name

    total_rating += film_rating

average_rating = total_rating / film_num

print(f"{highest_rated_film} is with highest rating: {max_rating:.1f}")
print(f"{lowest_rated_film} is with lowest rating: {min_rating:.1f}")
print(f'Average rating: {average_rating:.1f}')
