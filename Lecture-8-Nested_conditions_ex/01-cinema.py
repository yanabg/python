PREMIERE_PRICE = 12
NORMAL_PRICE = 7.50
DISCOUNT_PRICE = 5

screening_type = input().lower()
rows = int(input())
columns = int(input())

income = 0

cinema_capacity = rows * columns

if screening_type == "premiere":
    income = cinema_capacity * PREMIERE_PRICE
    # print(f"{income:.2f} leva")
elif screening_type == "normal":
    income = cinema_capacity * NORMAL_PRICE
    # print(f"{income:.2f} leva")
elif screening_type == "discount":
    income = cinema_capacity * DISCOUNT_PRICE
    # print(f"{income:.2f} leva")

print(f"{income:.2f} leva")