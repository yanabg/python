salary = 1500

while salary > 0:
    withdraw = int(input())
    if withdraw == -1:
        break
    salary -= withdraw
else:
    print("No more money")

print(salary)