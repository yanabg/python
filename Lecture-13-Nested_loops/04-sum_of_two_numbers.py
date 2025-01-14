interval_start = int(input())
interval_end = int(input())
magic_number = int(input())

combinations_counter = 0

is_found = False

# x1 + x2 + x3
for x1 in range(interval_start, interval_end + 1):
    for x2 in range(interval_start, interval_end + 1):
        combinations_counter += 1
        if x1 + x2 == magic_number:
            print(f'Combination N:{combinations_counter} ({x1} + {x2} = {magic_number})')
            is_found = True
            break
    if is_found:
        break
else:
    print(f'{combinations_counter} combinations - neither equals {magic_number}')


