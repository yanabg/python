# set constant
NOMINATION_THRESHOLD = 1250.5

# Read input:
name = input()
initial_points = float(input())
jury_count = int(input())

# Set points counter:
total_points = initial_points

# Loop through the jury
for _ in range(jury_count):
    assessor_name = input()
    score = float(input())

    # calc. points awarded
    points_awarded = (len(assessor_name) * score) / 2
    total_points += points_awarded

    if total_points >= NOMINATION_THRESHOLD:
        print(f'Congratulations, {name} got a nominee for leading role with {total_points:.1f}!')
        break
else:
    print(f'Sorry, {name} you need {NOMINATION_THRESHOLD - total_points:.1f} more!')
