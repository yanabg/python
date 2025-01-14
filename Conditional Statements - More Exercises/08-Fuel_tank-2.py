GASOLINE_PRICE = 2.22
GAS_PRICE = 0.93
DIESEL_PRICE = 2.33

GASOLINE_CARDHOLDER_DISCOUNT = 0.18
GAS_CARDHOLDER_DISCOUNT = 0.08
DIESEL_CARDHOLDER_DISCOUNT = 0.12

EXTRA_DISCOUNT_20_TO_25_LITERS = 0.08
EXTRA_DISCOUNT_MORE_THAN_25_LITERS = 0.10

fuel_type = input().lower()
fuel_quantity = float(input())
club_card = input().lower()

# base_price = 0

# Determine the base price:
if fuel_type == "gasoline":
    base_price = GASOLINE_PRICE
    if club_card == "yes":
        base_price -= GASOLINE_CARDHOLDER_DISCOUNT
elif fuel_type == "gas":
    base_price = GAS_PRICE
    if club_card == "yes":
        base_price -= GAS_CARDHOLDER_DISCOUNT
elif fuel_type == "diesel":
    base_price = DIESEL_PRICE
    if club_card == "yes":
        base_price -= DIESEL_CARDHOLDER_DISCOUNT
else:
    print(f"Invalid fuel type!")
    exit()

# Apply extra discounts based on quantity:
if fuel_quantity >= 20 and fuel_quantity <= 25:
    base_price *= (1 - EXTRA_DISCOUNT_20_TO_25_LITERS)
elif fuel_quantity > 25:
    base_price *= (1 - EXTRA_DISCOUNT_MORE_THAN_25_LITERS)

final_price = base_price * fuel_quantity
# print(f"fuel_type = {fuel_type}")
# print(f"base price: {base_price:.2f}")
print(f"{final_price:.2f} lv.")

