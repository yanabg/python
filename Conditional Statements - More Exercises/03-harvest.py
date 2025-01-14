from math import ceil, floor

WINE_PRODUCTIVITY = 0.40
GRAPES_FOR_1_L_WINE = 2.5

vineyard_in_sq_m = int(input())
grapes_per_sq_m = float(input())
wine_liters = int(input())
workers = int(input())

total_grapes = vineyard_in_sq_m * grapes_per_sq_m
wine = WINE_PRODUCTIVITY * total_grapes / GRAPES_FOR_1_L_WINE

if wine < wine_liters:
    remaining_wine = wine_liters - wine
    print(f"It will be a tough winter! More {floor(remaining_wine)} liters wine needed.")

elif wine >= wine_liters:
    remaining_wine = wine - wine_liters
    liters_per_person = remaining_wine / workers
    print(f"Good harvest this year! Total wine: {floor(wine)} liters.")
    print(f"{ceil(remaining_wine)} liters left -> {ceil(liters_per_person)} liters per person.")


