voucher_amount = int(input())
tickets_count, other_purchase_count = 0, 0

while True:
    purchase_name = input()

    if purchase_name == "End":
        break
    purchase_length = len(purchase_name)

    if purchase_length > 8: # => ticket
        purchase_cost = ord(purchase_name[0]) +\
                        ord(purchase_name[1])
        if purchase_cost > voucher_amount:
            break
        tickets_count += 1
    else: # <= 8 => other
        purchase_cost = ord(purchase_name[0])
        if purchase_cost > voucher_amount:
            break
        other_purchase_count += 1

    voucher_amount -= purchase_cost

print(tickets_count)
print(other_purchase_count)

