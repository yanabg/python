CALORIES_BURNT_PER_MINUTE = 5

minutes_walking = int(input())
walking_num = float(input())
calories_per_day = int(input())

total_walking_minutes = minutes_walking * walking_num
total_burnt_calories = total_walking_minutes * CALORIES_BURNT_PER_MINUTE

enough_walking_calories = 0.50 * calories_per_day

if total_burnt_calories >= enough_walking_calories:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {round(total_burnt_calories)}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {round(total_burnt_calories)}.')