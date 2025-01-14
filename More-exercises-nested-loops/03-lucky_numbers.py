num = int(input()) # numbers from 1 to 9

for first_digit in range(1, 10): #nums from 1 to 9, incl.
    for second_digit in range(1, 10): #  from 1 to 9, incl.
        for third_digit in range(1, 10): # nums from 1 to 9, incl.
            for fourth_digit in range(1, 10): # nums from 1 to 9, incl.
                sum_first_and_second = first_digit + second_digit
                sum_third_and_fourth = third_digit + fourth_digit
                if sum_first_and_second == sum_third_and_fourth and \
                        num % sum_first_and_second == 0:
                    print(f'{first_digit}{second_digit}{third_digit}{fourth_digit}', end=" ")
                else:
                    continue

