first_upper_limit = int(input())
second_upper_limit = int(input())
third_upper_limit = int(input())

for first_num in range(2, first_upper_limit + 1, 2): # start from 2 with step 2 => only even numbers
    for second_num in range(2, second_upper_limit + 1): # check if number is non-prime
        for third_num in range(2, third_upper_limit + 1, 2): # again only even numbers
            if second_num == 2 or \
                second_num == 3 or \
                second_num == 5 or \
                second_num == 7:
                # if all conditions above were met => print the valid pin code
                print(f'{first_num} {second_num} {third_num}')
            else:
                continue