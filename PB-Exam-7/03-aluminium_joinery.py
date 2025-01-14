# constant vars
SIZE_ONE_PRICE = 110
SIZE_TWO_PRICE = 140
SIZE_THREE_PRICE = 190
SIZE_FOUR_PRICE = 250

# read input
al_joinery_count = int(input())
al_joinery_type = input()
delivery_type = input()

base_price_per_window = 0
discount = 0

# determine base price and discount
if al_joinery_type == "90X130":
    if al_joinery_count > 60:
        discount = 0.08
    elif al_joinery_count > 30:
        discount = 0.05
    base_price_per_window = SIZE_TWO_PRICE
elif al_joinery_type == "100X150":
    if al_joinery_count > 80:
        discount = 0.10
    elif al_joinery_count > 40:
        discount = 0.06
    base_price_per_window = SIZE_TWO_PRICE
elif al_joinery_type == "130X180":
    if al_joinery_count > 50:
        discount = 0.12
    elif al_joinery_count > 20:
        discount = 0.07
    base_price_per_window = SIZE_THREE_PRICE
elif al_joinery_type == "200X300":
    if al_joinery_count > 25:
        discount = 0.09
    elif al_joinery_count > 50:
        discount = 0.14
    base_price_per_window = SIZE_FOUR_PRICE

# calc total price
total_price = base_price_per_window * al_joinery_count

# apply the discounts
if al_joinery_count < 10:
    print("Invalid order")
else:
    total_price -= total_price * discount

    # delivery cost
    if delivery_type == "With delivery":
        total_price += 60

    # extra discount for > 99
    if al_joinery_count > 99:
        total_price *= 0.96

    print(f'{total_price:.2f} BGN')
