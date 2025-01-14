PREMIERE_TICKET = 12
NORMAL_TICKET = 7.50
DISCOUNT_TICKET = 5

type_movie = input()

# 1st input goes to rows, the 2nd to cols -> same as to write 2 diff.variables on 2 separate lines:
rows, cols = int(input()), int(input())

income = 0
cinema_hall_capacity = rows * cols

if type_movie == "Premiere":
    income = cinema_hall_capacity * PREMIERE_TICKET
elif type_movie == "Normal":
    income = cinema_hall_capacity * NORMAL_TICKET
elif type_movie == "Discount":
    income = cinema_hall_capacity * DISCOUNT_TICKET

print(f'{income:.2f} leva')

