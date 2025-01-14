students_num = int(input())

top_students_count = 0
between_4_and_4_99_count = 0
between_3_and_3_99_count = 0
fail_count = 0
total_sum = 0

# read grades
for _ in range(students_num):
    grade = float(input())
    total_sum += grade

    if grade < 3.00:
        fail_count += 1
    elif 3.00 <= grade <= 3.99:
        between_3_and_3_99_count += 1
    elif 4.00 <= grade <= 4.99:
        between_4_and_4_99_count += 1
    elif grade >= 5.00:
        top_students_count += 1

# calc %-s:
top_students_percentage = (top_students_count / students_num) * 100
between_4_and_4_99_percentage = (between_4_and_4_99_count / students_num) * 100
between_3_and_3_99_percentage = (between_3_and_3_99_count / students_num) * 100
fail_percentage = (fail_count / students_num) * 100

average_grade = total_sum / students_num

print(f"Top students: {top_students_percentage:.2f}%")
print(f"Between 4.00 and 4.99: {between_4_and_4_99_percentage:.2f}%")
print(f"Between 3.00 and 3.99: {between_3_and_3_99_percentage:.2f}%")
print(f"Fail: {fail_percentage:.2f}%")
print(f"Average: {average_grade:.2f}")
