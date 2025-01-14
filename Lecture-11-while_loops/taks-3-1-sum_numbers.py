CONSTANT_NUMBER = int(input())
sum_numbers = 0

# using while true
while True:
    current_num = int(input())
    sum_numbers += current_num
    if sum_numbers >= CONSTANT_NUMBER:
        print(sum_numbers)
        break

