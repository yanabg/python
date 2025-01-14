# items price
BASKET_PRICE = 1.50
WREATH_PRICE = 3.80
CHOCOLATE_BUNNY = 7.00

# clients count
num_clients = int(input())

# counter to store total amount
total_sum = 0

# loop over eac client
for _ in range(num_clients):
    # counter to store items number and the sum per client
    items_count = 0
    client_sum = 0

    while True:
        item = input()
        if item == "Finish":
            break
        items_count += 1

        if item == "basket":
            client_sum += BASKET_PRICE
        elif item == "wreath":
            client_sum += WREATH_PRICE
        elif item == "chocolate bunny":
            client_sum += CHOCOLATE_BUNNY

        # check for discount after processing all items
    if items_count % 2 == 0:
        client_sum *= 0.80

    # print current client's total'
    print(f'You purchased {items_count} items for {client_sum:.2f} leva.')

    total_sum += client_sum

# Calculate and print the average bill per client
average_bill = total_sum / num_clients
print(f'Average bill per client is: {average_bill:.2f} leva.')
