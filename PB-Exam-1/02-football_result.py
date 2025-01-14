match_one_result = input()
match_two_result = input()
match_three_result = input()

wins = 0
losses = 0
draws = 0

home_score_one = int(match_one_result[0])
guest_score_one = int(match_one_result[2])

if home_score_one > guest_score_one:
    wins += 1
elif home_score_one < guest_score_one:
    losses += 1
else:
    draws += 1

home_score_two = int(match_two_result[0])
guest_score_two = int(match_two_result[2])

if home_score_two > guest_score_two:
    wins += 1
elif home_score_two < guest_score_two:
    losses +=1
else:
    draws +=1

home_score_three = int(match_three_result[0])
guest_score_three = int(match_three_result[2])

if home_score_three > guest_score_three:
    wins += 1
elif home_score_three < guest_score_three:
    losses += 1
else:
    draws += 1

print(f'Team won {wins} games.')
print(f'Team lost {losses} games.')
print(f'Drawn games: {draws}')