target_amount = float(input())

collected_amount, card_payments, cash_payments, cash_count, card_count, transaction_counter = 0, 0, 0, 0, 0, 0

while collected_amount < target_amount:
    command = input()

    if command == "End":
        print(f'Failed to collect required money for charity.')
        break

    items_price = int(command)
    transaction_counter += 1

    if transaction_counter % 2 != 0: # cash pmt
        if items_price > 100:
            print('Error in transaction!')
        else:
            print('Product sold!')
            collected_amount += items_price
            cash_payments += items_price
            cash_count += 1
    else: #card pmt
        if items_price < 10:
            print('Error in transaction!')
        else:
            print('Product sold!')
            collected_amount += items_price
            card_payments += items_price
            card_count += 1

if collected_amount >= target_amount:
    average_cash = cash_payments / cash_count if cash_count > 0 else 0
    average_card = card_payments / card_count if card_count > 0 else 0
    print(f'Average CS: {average_cash:.2f}')
    print(f'Average CC: {average_card:.2f}')


