days = int(input())
total_food = float(input())

total_dog_food = 0
total_cat_food = 0
total_biscuit = 0

# for each day in days require input for dog food and cat food
for day in range(1, days + 1):
    dog_food = int(input())
    cat_food = int(input())

    # then update food quantity for dogs and cats
    total_dog_food += dog_food
    total_cat_food += cat_food

    # check each 3rd day
    if day % 3 == 0:
        total_biscuit += 0.10 * (dog_food + cat_food)

total_eaten_food = total_dog_food + total_cat_food

percent_eaten_food = (total_eaten_food / total_food) * 100
percent_dog = (total_dog_food / total_eaten_food) * 100
percent_cat = (total_cat_food / total_eaten_food) * 100

print(f'Total eaten biscuits: {round(total_biscuit)}gr.')
print(f'{percent_eaten_food:.2f}% of the food has been eaten.')
print(f'{percent_dog:.2f}% eaten from the dog.')
print(f'{percent_cat:.2f}% eaten from the cat.')




