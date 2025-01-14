protective_plastic_price = 1.5
paint_price = 14.50
paint_thinner_price = 5.00
extra_bags = 0.4

plastic_quantity = int(input())
paint_quantity = int(input())
paint_thinner_quantity = int(input())
hours_of_work = int(input())


cost_paint = (paint_quantity * 1.1) * paint_price
# print(f"Total cost for paint is {cost_paint}")

cost_plastic = (plastic_quantity + 2) * protective_plastic_price
# print(f"Total cost for plastic is {cost_plastic}")

cost_thinner = paint_thinner_quantity * paint_thinner_price
# print(f"Total cost for thinner is {cost_thinner}")

total_materials_cost = cost_paint + cost_plastic + cost_thinner + extra_bags
# print(f"Total cost for materials is {total_materials_cost}")

cost_work = (total_materials_cost * 0.3) * hours_of_work
# print(f"Total cost for work is {cost_work}")

total_cost = total_materials_cost + cost_work
# print(f"Total cost for everything is {total_cost}")
print(total_cost)