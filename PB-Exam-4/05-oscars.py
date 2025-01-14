NOMINATION_LIMIT = 1250.5

player_name = input()
initial_jury_points = float(input())
jury_members = int(input())

total_points = initial_jury_points

for _ in range(jury_members):
    jury_member_name = input()
    current_score = float(input())

    points_awarded = (len(jury_member_name) * current_score) / 2
    total_points += points_awarded

    if total_points >= NOMINATION_LIMIT:
        print(f'Congratulations, {player_name} got a nominee for leading role with {total_points:.1f}!')
        break
else:
    print(f'Sorry, {player_name} you need {NOMINATION_LIMIT - total_points:.1f} more!')

