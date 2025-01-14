n1 = int(input())
n2 = int(input())
operator = input()

result = 0
result_type = ""

if operator == "+":
    result = n1 + n2
    if result % 2 == 0:
        result_type = "even"
    else:
        result_type = "odd"
    print(f"{n1} {operator} {n2} = {result} - {result_type}")
elif operator == "-":
    result = n1 - n2
    if result % 2 == 0:
        result_type = "even"
    else:
        result_type = "odd"
    print(f"{n1} {operator} {n2} = {result} - {result_type}")
elif operator == "*":
    result = n1 * n2
    if result % 2 == 0:
        result_type = "even"
    else:
        result_type = "odd"
    print(f"{n1} {operator} {n2} = {result} - {result_type}")
elif operator == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 / n2
        print(f"{n1} / {n2} = {result:.2f}")
elif operator == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        remainder = n1 % n2
        print(f"{n1} % {n2} = {remainder}")
