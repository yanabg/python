student_name = input()
grades_total = 0  # sum of all grades
years_counter = 0  # count of years with bad grade
failed_years = 0  # count if years when failing

while years_counter < 12:
    annual_grade = float(input())

    if annual_grade < 4:
        failed_years += 1
        if failed_years == 2:
            excluded_year = years_counter + 1
            print(f'{student_name} has been excluded at {excluded_year} grade')
            break
        continue

    years_counter += 1
    grades_total += annual_grade  # add annual grade to the total grades

else:
    average_grade = grades_total / 12
    print(f'{student_name} graduated. Average grade: {average_grade:.2f}')