visitors_count = int(input())

back_count = 0
chest_count = 0
legs_count = 0
abs_count = 0
protein_shake_count = 0
protein_bar_count = 0

for _ in range(visitors_count):
    exercise = input()
    if exercise == "Back":
        back_count += 1
    elif exercise == "Chest":
        chest_count += 1
    elif exercise == "Legs":
        legs_count += 1
    elif exercise == "Abs":
        abs_count += 1
    elif exercise == "Protein shake":
        protein_shake_count += 1
    elif exercise == "Protein bar":
        protein_bar_count += 1

workout_count = back_count + chest_count + legs_count + abs_count
protein_count = protein_shake_count + protein_bar_count

percent_workout = (workout_count / visitors_count) * 100
percent_protein = (protein_count / visitors_count) * 100

print(f'{back_count} - back')
print(f'{chest_count} - chest')
print(f'{legs_count} - legs')
print(f'{abs_count} - abs')
print(f'{protein_shake_count} - protein shake')
print(f'{protein_bar_count} - protein bar')
print(f'{percent_workout:.2f}% - work out')
print(f'{percent_protein:.2f}% - protein')


