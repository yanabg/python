from math import floor, ceil

days = int(input())
food_left_kg = float(input())
daily_food_deer_one = float(input())
daily_food_deer_two = float(input())
daily_food_deer_three = float(input())

deer_one = daily_food_deer_one * days
deer_two = daily_food_deer_two * days
deer_three = daily_food_deer_three * days

total_food_needed = deer_one + deer_two + deer_three

if food_left_kg >= total_food_needed:
    print(f'{floor(food_left_kg - total_food_needed)} kilos of food left.')
else:
    print(f'{ceil(total_food_needed - food_left_kg)} more kilos of food are needed.')
