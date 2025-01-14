bottles = int(input())
detergent_quantity = bottles * 750 # 1 bottle = 750 ml.

clean_dishes, clean_pots, load_counter = 0, 0, 0

while True:
    command = input()

    if command == "End":
        break

    dishes_count = int(command)
    load_counter += 1

    if load_counter % 3 == 0:
        detergent_used = 15 * dishes_count
        clean_pots += dishes_count
    else:
        detergent_used = 5 * dishes_count
        clean_dishes += dishes_count

    detergent_quantity -= detergent_used

    if detergent_quantity < 0:
        print(f'Not enough detergent, {abs(detergent_quantity)} ml. more necessary!')
        break

if detergent_quantity >= 0:
    print(f'Detergent was enough!')
    print(f'{clean_dishes} dishes and {clean_pots} pots were washed.')
    print(f'Leftover detergent {detergent_quantity} ml.')

