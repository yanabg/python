INITIAL_FEE_TAXI = 0.70
TAXI_DAY_PER_KM = 0.79
TAXI_NIGHT_PER_KM = 0.90

BUS_FEE_KM = 0.09
BUS_MIN_DISTANCE_KM = 20

TRAIN_FEE_KM = 0.06
TRAIN_MIN_DISTANCE_KM = 100

distance = int(input())
part_of_the_day = str(input())

if distance < BUS_MIN_DISTANCE_KM:
    if part_of_the_day == "day":
        price_taxi_day = INITIAL_FEE_TAXI + distance * TAXI_DAY_PER_KM
        #        print(f"taxi day price: {price_taxi_day}")
        print(f"{price_taxi_day:.2f}")
    else:
        price_taxi_night = INITIAL_FEE_TAXI + distance * TAXI_NIGHT_PER_KM
        #        print(f"price night taxi: {price_taxi_night}")
        print(f"{price_taxi_night:.2f}")
elif distance >= TRAIN_MIN_DISTANCE_KM:
    price_train = distance * TRAIN_FEE_KM
    #    print(f"price train: {price_train}")
    print(f"{price_train:.2f}")
else:
    price_bus = distance * BUS_FEE_KM
    #    print(f"price bus: {price_bus}")
    print(f"{price_bus:.2f}")
