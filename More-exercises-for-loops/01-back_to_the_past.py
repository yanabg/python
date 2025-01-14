inherited_amount = float(input())
target_year = int(input())

start_year = 1800
ivanch_age = 18
current_amount = inherited_amount

# Iterate through each year from 1800 to target_year inclusive
for year in range(start_year, target_year + 1):
    if year % 2 == 0: # even year
        yearly_expense = 12000
    else: # odd year
        years_passed = year - start_year
        yearly_expense = 12000 + 50 * ivanch_age

    # Deduct the yearly expense from the current mamount
    current_amount -= yearly_expense

    # Increase Ivanch's age by 1 year each year
    ivanch_age += 1

if current_amount >= 0:
    print(f'Yes! He will live a carefree life and will have {current_amount:.2f} dollars left.')
else:
    print(f'He will need {abs(current_amount):.2f} dollars to survive.')