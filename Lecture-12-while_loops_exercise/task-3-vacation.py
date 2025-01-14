needed_money = float(input())
available_money = float(input())

days_counter = 0
spending_counter = 0

while available_money < needed_money and spending_counter < 5:
    action_type = input()
    action_amount = float(input())
    days_counter += 1

    if action_type == "save":
        available_money += action_amount
        spending_counter = 0
    elif action_type == "spend":
        available_money -= action_amount
        spending_counter += 1
        if available_money < 0:
            available_money = 0
if spending_counter == 5:
    print('You can\'t save the money.')
    print(days_counter)

if available_money >= needed_money:
    print(f'You saved the money for {days_counter} days.')