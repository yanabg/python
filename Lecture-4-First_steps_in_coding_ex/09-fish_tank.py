length = int(input())
width = int(input())
height = int(input())
percentage = float(input())


tank_volume = length * width * height
tank_vol_liters = tank_volume / 1000
required_liters = tank_vol_liters * (1-percentage/100)

print(f"tank volume is: {tank_volume}")
print(f"tank_vol_liters is: {tank_vol_liters}")
print(f"required_liters is: {required_liters}")
