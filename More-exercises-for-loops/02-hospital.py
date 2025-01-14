period = int(input())

initial_doctors_num = 7
total_examined = 0
total_non_examined = 0
doctors_num = initial_doctors_num

for day in range(1, period + 1):
    daily_patients = int(input())

    # Check every third day and increase the number of doctors if necessary
    if day % 3 == 0 and total_non_examined > total_examined:
        doctors_num += 1

    if daily_patients <= doctors_num:
        examined_patients = daily_patients
        non_examined_patients = 0
    else:
        examined_patients = doctors_num
        non_examined_patients = daily_patients - examined_patients

    total_examined += examined_patients
    total_non_examined += non_examined_patients

print(f'Treated patients: {total_examined}.')
print(f'Untreated patients: {total_non_examined}.')
