start_interval = int(input())
end_interval = int(input())
magic_number = int(input())

# set counters:
combination_count = 0
found_combination = False
first_number = 0
seconds_number = 0

# loop over all combinations within this interval
for first in range(start_interval, end_interval + 1):
    for second in range(start_interval, end_interval +1):
        combination_count += 1
        if first + second == magic_number:
            found_combination = True
            print(f'Combination N:{combination_count} ({first} + {second} = {magic_number})')
            break
    if found_combination:
        break

# if no combination was found:
if not found_combination:
    print(f'{combination_count} combinations - neither equals {magic_number}')