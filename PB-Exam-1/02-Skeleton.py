TIME_REDUCTION = 2.5

minutes = int(input())
seconds = int(input())
length = float(input())
targeted_seconds_for_100_m = float(input())

length_seconds = minutes * 60 + seconds
count_time_reductions = length / 120
total_reduced_time = count_time_reductions * TIME_REDUCTION

# print(f'length seconds: {length_seconds}')
# print(f'count time reductions: {count_time_reductions}')
# print(f'totla reduced time: {total_reduced_time}')

time_marin = (length / 100) * targeted_seconds_for_100_m - total_reduced_time
# print(f'time Marin: {time_marin}')

if time_marin <= length_seconds:
    print(f'Marin Bangiev won an Olympic quota!')
    print(f'His time is {time_marin:.3f}.')
else:
    print(f'No, Marin failed! He was {abs(length_seconds - time_marin):.3f} second slower.')