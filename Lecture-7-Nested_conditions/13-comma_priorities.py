number1 = int(input())
number2 = int(input())
number3 = int(input())

if (number1 >= number2 and number2 <= 200) or (number3 + number2 >= 300 and number3 <= 400):
    print("yes") # Yes
if number1 > 100 and (number2 <= 200 or number3 + number2 >= 300) and number3 <= 400:
    print("Yes") # No output