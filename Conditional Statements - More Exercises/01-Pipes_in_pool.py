v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

pipe1 = p1 * h
# print(f"pipe1 is: {pipe1}")

pipe2 = p2 * h
# print(f"pipe 2 is: {pipe2}")

total_fill_in = pipe1 + pipe2
# print(f'total filled in: {total_fill_in}')

if total_fill_in <= v:
    pipe1_share = (pipe1 / total_fill_in) * 100
    pipe2_share = (pipe2 / total_fill_in) * 100
    total_share = (total_fill_in / v) * 100
#    print(f"pipe1 share is:{pipe1_share:.2f}%")
#    print(f"pipe2 share is:{pipe2_share:.2f}%")
    print(f"The pool is:{total_share:.2f}% full. Pipe 1: {pipe1_share:.2f}%. Pipe 2: {pipe2_share:.2f}%.")

else:
    excess_water = total_fill_in - v
    # print(f"excess water: {excess_water:.2f}")
    print(f"For: {h} hours the pool overflows with {excess_water:.2f} liters.")

