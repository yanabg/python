failures_threshold = int(input())

failed_tasks_count = 0
solved_tasks_count = 0
all_grades_sum = 0
last_task = None
has_failed = True

while failed_tasks_count < failures_threshold:
    task_name = input()
    if task_name == "Enough":
        has_failed = False
        break

    grade = int(input())
    if grade <= 4:
        failed_tasks_count += 1
    all_grades_sum += grade
    solved_tasks_count += 1
    last_task = task_name

if has_failed:
    print(f'You need a break, {failed_tasks_count} poor grades.')
else:
#    print(f'all grades sum is: {all_grades_sum}')
    print(f'Average score: {all_grades_sum / solved_tasks_count:.2f}')
    print(f'Number of problems: {solved_tasks_count}')
    print(f'Last problem: {last_task}')

