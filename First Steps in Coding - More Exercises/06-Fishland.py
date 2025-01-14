PRICE_MIDI_KG = 7.5

price_skumriya_za_kg = float(input())
price_caca_za_kg = float(input())

quantity_palamud_kg = float(input())
quantity_safrid_kg = float(input())
quantity_midi_kg = int(input())

price_palamud_kg = 1.6 * price_skumriya_za_kg
price_safrid_kg = 1.8 * price_caca_za_kg


# print(f"price_palamud: {price_palamud_kg}")
# print(f"price_safrid: {price_safrid_kg}")

total_price = (quantity_palamud_kg * price_palamud_kg) + (quantity_safrid_kg * price_safrid_kg) + (quantity_midi_kg * PRICE_MIDI_KG)

print(f"{total_price:.2f}")

