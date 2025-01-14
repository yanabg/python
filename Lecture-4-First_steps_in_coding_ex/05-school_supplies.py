pen_packets = int(input())
markers_packets = int(input())
detergent_liters = int(input())
discount_percentage = int(input())/100

pen_pckt_price = 5.8
marker_pckt_price = 7.2
detergent_per_liter_price = 1.2

total_cost_pens_before_discount = pen_packets * pen_pckt_price
total_cost_markers_before_discount = markers_packets * marker_pckt_price
total_cost_deterg_before_disc = detergent_liters * detergent_per_liter_price

pen_discount = discount_percentage * total_cost_pens_before_discount
marker_discount = discount_percentage * total_cost_markers_before_discount
detergent_discount = discount_percentage * total_cost_deterg_before_disc

pens_final_price = total_cost_pens_before_discount - pen_discount
markers_final_price = total_cost_markers_before_discount - marker_discount
detergent_final_price = total_cost_deterg_before_disc - detergent_discount

total_price_before_discount = total_cost_pens_before_discount + total_cost_markers_before_discount + total_cost_deterg_before_disc

reduced_total = total_price_before_discount - (total_price_before_discount * discount_percentage)

print(reduced_total)

# print("Costs before discount: ")
# print(total_cost_pens_before_discount)
# print(total_cost_markers_before_discount)
# print(total_cost_detergent_before_discount)

# print("total price before discount: ")
# print(total_price_before_discount)



