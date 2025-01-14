CORRIDOR = 100
WORK_SPACE_HEIGHT = 70
WORK_SPACE_WIDTH = 120

width_in_m = float(input())
height_in_m = float(input())


hall_height_in_centimeters = height_in_m * 100
hall_width_in_centimeters = width_in_m * 100

desks_per_row = (hall_height_in_centimeters - CORRIDOR) // WORK_SPACE_HEIGHT
desks_per_line = hall_width_in_centimeters // WORK_SPACE_WIDTH

number_of_desks = desks_per_row * desks_per_line - 3

# print(f"desks per row: {desks_per_row}")
# print(f"desks per line: {desks_per_line}")
print(f"{number_of_desks:.0f}")


