import math

wall_height = int(input())
wall_width = int(input())
percent_non_paint = float(input())

total_surface_size = wall_height * wall_width * 4
walls_to_paint = math.ceil(total_surface_size * (1 - percent_non_paint / 100))

while True:
    command = input()

    if command == "Tired!":
        print(f'{walls_to_paint} quadratic m left.')
        break

    liters_paint = int(command)
    walls_to_paint -= liters_paint # 1 liter paints 1 sq.m.

    if walls_to_paint <= 0:
        if walls_to_paint == 0:
            print(f'All walls are painted! Great job, Pesho!')
        else:
            print(f'All walls are painted and you have {abs(walls_to_paint)} l paint left!')
        break

