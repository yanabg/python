target_profit = float(input())  # Read the desired profit target
total_income = 0  # Initialize total income to zero

while True:
    cocktail_name = input()  # Read the name of the cocktail
    if cocktail_name == "Party!":
        break  # Exit the loop if "Party!" is entered

    cocktail_num = int(input())  # Read the number of cocktails ordered
    cocktail_price = len(cocktail_name)  # Price of each cocktail is its name length
    total_price = cocktail_num * cocktail_price  # Total price for this order

    # Apply discount if the total price is odd
    if total_price % 2 != 0:
        total_price *= 0.75  # Apply 25% discount to total price

    total_income += total_price  # Add total price to the total income

    # Check if the target profit is reached or exceeded
    if total_income >= target_profit:
        print("Target acquired.")
        print(f"Club income - {total_income:.2f} leva.")
        break

# If total income is less than target profit, calculate and print the shortfall
if total_income < target_profit:
    print(f"We need {target_profit - total_income:.2f} leva more.")
    print(f"Club income - {total_income:.2f} leva.")
