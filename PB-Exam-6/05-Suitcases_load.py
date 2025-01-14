capacity = float(input())

used_capacity = 0
suitcase_count = 0

while True:
    command = input()
    if command == 'End':
        print('Congratulations! All suitcases are loaded!')
        break

    suitcase_volume = float(command)
    suitcase_count += 1

    if suitcase_count % 3 == 0:
        suitcase_volume *= 1.10

    if used_capacity + suitcase_volume > capacity:
        print('No more space!')
        suitcase_count -= 1 # this suitcase wont be loaded => decrement
        break

    used_capacity += suitcase_volume

print(f'Statistic: {suitcase_count} suitcases loaded.')
