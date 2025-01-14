MIN_BAD_GRADES_COUNT = 4

max_bad_grades_threshold = int(input())

current_bad_grades = 0
total_grades = 0
grades_sum = 0
last_task = None

while current_bad_grades < max_bad_grades_threshold:
    task_name= input() # we'll read grade after the of=="Enough
    # grade = int(input) -> because task_name==Enough -> can't ne int => we'll remain empty
    if task_name == "Enough":
        print(f'Average score: {grades_sum / total_grades:.2f}')
        print(f'Number of problems: {total_grades}')
        print(f'Last problem: {last_task}')
        break

    grade = int(input())

    if grade <= MIN_BAD_GRADES_COUNT:
        current_bad_grades += 1

    grades_sum += grade
    total_grades += 1
    last_task = task_name

else:
    print(f'You need a break, {current_bad_grades} poor grades.')

