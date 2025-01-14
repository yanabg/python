iteration_counter = 0
for hours in range(0, 24):
    for minutes in range(1, 60):
        for seconds in range(0, 60):
            iteration_counter += 1
            print(f'{hours}:{minutes:02d}:{seconds:02d}')

print(f'Number of iterations: {iteration_counter}')
