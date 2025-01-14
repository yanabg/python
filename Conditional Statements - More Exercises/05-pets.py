from math import ceil, floor

days = int(input())
food_left_kg = int(input())
food_dog_kg = float(input())
food_cat_kg = float(input())
food_turtle_grams = float(input())

dog_food_need = days * food_dog_kg
cat_food_need = days * food_cat_kg
turtle_food_need = days * food_turtle_grams/1000

"""
print(dog_food_need)
print(cat_food_need)
print(turtle_food_need)
"""

total_food_needed = dog_food_need + cat_food_need + turtle_food_need
# print(total_food_needed)

if total_food_needed <= food_left_kg:
    remaining_food = food_left_kg - total_food_needed
    print(f"{floor(remaining_food)} kilos of food left.")
elif total_food_needed > food_left_kg:
    insufficient_food = total_food_needed - food_left_kg
    print(f"{ceil(insufficient_food)} more kilos of food are needed.")
