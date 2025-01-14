from math import pi

figure = str(input())
area = 0;

if figure == "square":
    side_length = float(input())
    area = side_length * side_length

elif figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b

elif figure == "circle":
    radius = float(input())
    area = pi * radius ** 2

elif figure == "triangle":
    side = float(input())
    height = float(input())
    area = 0.5 * side * height

print(f"{area:.3f}")
