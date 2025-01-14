from math import  ceil

film_name = input()
film_length = int(input())
break_length = int(input())

lunch_time = break_length / 8
leisure_time = break_length / 4

time_needed = lunch_time + leisure_time + film_length
time_left = break_length - time_needed

if time_left >= 0:
    print(f"You have enough time to watch {film_name} and left with {ceil(time_left)} minutes free time.")
else:
    print(f"You don't have enough time to watch {film_name}, you need {ceil(abs(time_left))} more minutes.")
