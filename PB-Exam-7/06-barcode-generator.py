first_number = input()
second_number = input()

f1, f2, f3, f4 = int(first_number[0]), int(first_number[1]), int(first_number[2]), int(first_number[3])
s1, s2, s3, s4 = int(second_number[0]), int(second_number[1]), int(second_number[2]), int(second_number[3])

for num1 in range(f1, s1 + 1):
    for num2 in range(f2, s2 + 1):
        for num3 in range(f3, s3 + 1):
            for num4 in range(f4, s4 + 1):
                if num1 % 2 != 0 and num2 % 2 != 0 and num3 % 2 != 0 and num4 % 2 != 0:
                    print(f'{num1}{num2}{num3}{num4}', end=" ")