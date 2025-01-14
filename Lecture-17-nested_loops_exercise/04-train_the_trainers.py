jury_count = int(input())

total_grades = 0 # No of presentations
total_grades_sum = 0 # sum the marks

while True:
    presentation_name = input()

    if presentation_name == "Finish":
        break

    grades_sum = 0

    for _ in range(jury_count):
        grades_sum += float(input())

    total_grades += jury_count
    total_grades_sum += grades_sum

    print(f"{presentation_name} - {grades_sum / jury_count:.2f}.")

print(f"Student's final assessment is {total_grades_sum / total_grades:.2f}.")