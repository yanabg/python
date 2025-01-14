food_quantity_kg = int(input())

food_quantity_grams = food_quantity_kg * 1000
total_food_eaten = 0

while True:
    food_eaten_grams_per_eat = input()
    if food_eaten_grams_per_eat == "Adopted":
        break

    food_eaten_per_eat = int(food_eaten_grams_per_eat)
    total_food_eaten += food_eaten_per_eat

if total_food_eaten <= food_quantity_grams:
    print(f'Food is enough! Leftovers: {food_quantity_grams - total_food_eaten} grams.')
else:
    print(f'Food is not enough. You need {total_food_eaten - food_quantity_grams} grams more.')


