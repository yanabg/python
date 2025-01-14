available_sum = 0

while True:
    inpt = input()
    if inpt == "NoMoreMoney":
        break
    current_sum = float(inpt)

    if current_sum < 0:
        print(f'Invalid operation!')
        break

    available_sum += current_sum
    print(f'Increase: {current_sum:.2f}')

print(f'Total: {available_sum:.2f}')