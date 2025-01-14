x = float(input())
y = float(input())
h = float(input())

WINDOW = 1.5
GREEN_PAINT_PER_LITER = 3.4
RED_PAINT_PER_LITER = 4.3

side_wall_area = x * y
# print(f'side wall area is: {side_wall_area:.2f}')

front_wall = x ** 2
# print(f'front wall area is: {front_wall:.2f}')

window_area = 1.5 * 1.5
# print(f'window area is: {window_area:.2f}')

door_area = 2 * 1.2
# print(f'door area is: {door_area:.2f}')

wall_sides = (2 * side_wall_area) - (2 * window_area)
# print(f'wall_sides: {wall_sides:.2f}')

wall_fronts = (2 * front_wall) - door_area
#print(f'wall front sides: {wall_fronts:.2f}')

walls_total_area = wall_fronts + wall_sides
# print(f'walls total area is: {walls_total_area:.2f}')

green_paint = walls_total_area / GREEN_PAINT_PER_LITER
print(f'{green_paint:.2f}')

roof_squares = 2 * (x * y)
# print(f'roof squares: {roof_squares:.2f}')

roof_triangles = 2 * (x * h / 2)
# print(f'roof triangles: {roof_triangles:.2f}')

total_roof_area = roof_squares + roof_triangles
# print(f'total_roof_area is: {total_roof_area:.2f}')

red_paint = total_roof_area / RED_PAINT_PER_LITER
print(f'{red_paint:.2f}')
