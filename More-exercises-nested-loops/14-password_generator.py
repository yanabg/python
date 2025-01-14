n = int(input())
l = int(input())

# Iterate over the first digit (1 to n)
for first_digit in range(1, n + 1):
    # Iterate over the second digit (1 to n)
    for second_digit in range(1, n + 1):
        # Iterate over the third character (first l lowercase letters)
        for third_char in range(97, 97 + l):
            # Iterate over the fourth character (first l lowercase letters)
            for fourth_char in range(97, 97 + l):
                # Iterate over the fifth digit (1 to n, must be greater than first and second digits)
                for fifth_digit in range(1, n + 1):
                    if fifth_digit > first_digit and fifth_digit > second_digit:
                        # Print the valid password
                        print(f'{first_digit}{second_digit}{chr(third_char)}{chr(fourth_char)}{fifth_digit}', end=" ")

