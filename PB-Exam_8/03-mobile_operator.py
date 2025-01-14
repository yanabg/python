contract_term = input()
contract_type = input()
has_mobile_internet = input()
months_to_pay = int(input())

price = 0
mobile_net_uplift = 0

if contract_term == "one":
    if contract_type == "Small":
        price = 9.98
    elif contract_type == "Middle":
        price = 18.99
    elif contract_type == "Large":
        price = 25.98  # Corrected to match the second code
    elif contract_type == "ExtraLarge":
        price = 35.99
elif contract_term == "two":
    if contract_type == "Small":
        price = 8.58
    elif contract_type == "Middle":
        price = 17.09
    elif contract_type == "Large":
        price = 23.59
    elif contract_type == "ExtraLarge":
        price = 31.79

if has_mobile_internet == "yes":
    if price <= 10:
        mobile_net_uplift = 5.50
    elif price <= 30:
        mobile_net_uplift = 4.35
    elif price > 30:
        mobile_net_uplift = 3.85

monthly_price = price + mobile_net_uplift
total_price = monthly_price * months_to_pay

if contract_term == "two":
    total_price *= 0.9625

print(f'{total_price:.2f} lv.')
