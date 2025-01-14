session_time = int(input())
scenes_num = int(input())
duration = int(input())

preparation = session_time * 0.15
scenes_shooting_time = scenes_num * duration

required_time = preparation + scenes_shooting_time

if required_time > session_time:
    print(f'Time is up! To complete the movie you need {round(required_time - session_time)} minutes.')
else:
    print(f'You managed to finish the movie on time! You have {round(session_time - required_time)} minutes left!')