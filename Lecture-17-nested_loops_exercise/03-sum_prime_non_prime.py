from math import sqrt

sum_prime, sum_non_prime = 0, 0

while True:
    command = input() # number or Stop

    if command == "stop":
        break

    current_number = int(command) # if comamnd is not stop => we want int from the input in command

    if current_number < 0:
        print("Number is negative.")
        continue

    # each number can be / to 1 => we start from 2
    # sqrt as in math we check up to the sqrt of the number
    for number in range(2, int(sqrt(current_number)) + 1):
        if current_number % number == 0:
            sum_non_prime += current_number
            break
    else:
        sum_prime += current_number

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")