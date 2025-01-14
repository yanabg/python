price_1_dog_pckt = 2.5
price_1_cat_pck = 4

pckt_num_dog = int(input())
pckt_num_cat = int(input())

end_price = (pckt_num_dog * price_1_dog_pckt) + (pckt_num_cat * price_1_cat_pck)

print(f"{end_price} lv.")