MAX_DAYS_SPENDING = 5

vacation_price = float(input())
balance = float(input())

days_spending_counter = 0
total_days_counter = 0

while days_spending_counter < MAX_DAYS_SPENDING:
    action = input() # spend or safe
    money = float(input())
    total_days_counter += 1

    if action == "spend":
        # option 1:
        # balance = balance - money if balance > money else 0

        # option 2: most optimal one
        balance -= money if balance > money else balance
        days_spending_counter +=1

        # option 3:
        # if balance > money:
        #     balance -= money
        # else:
        #     balance = 0
    else:
        balance += money
        days_spending_counter = 0

        if balance >= vacation_price:
            print(f'You saved the money for {total_days_counter} days.')
            break

else:
    print('You can\'t save the money.')
    print(total_days_counter)
