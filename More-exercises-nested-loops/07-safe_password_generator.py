a = int(input())
b = int(input())
max_password_count = int(input())

A = 35
B = 64
password_count = 0

for first_num in range(1, a + 1):
    for second_num in range(1, b + 1):
        if password_count >= max_password_count:
            break

        print(f'{chr(A)}{chr(B)}{first_num}{second_num}{chr(B)}{chr(A)}', end="|")
        password_count += 1

        A += 1
        if A > 55:
            A = 35

        B += 1
        if B > 96:
            B = 64


