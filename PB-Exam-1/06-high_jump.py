target_height = int(input())
current_height = target_height - 30

total_jumps = 0
failed_attempts = 0

while current_height <= target_height:
    jump = int(input())
    total_jumps += 1

    if jump > current_height:
        current_height += 5
        failed_attempts = 0

        if current_height > target_height:
            print(f'Tihomir succeeded, he jumped over {current_height - 5}cm after {total_jumps} jumps.')
            break
    else:
        failed_attempts += 1
        if failed_attempts == 3:
            print(f'Tihomir failed at {current_height}cm after {total_jumps} jumps.')
            break