dish_name = input("Введіть назву страви: ")
quantity = int(input("Введіть кількість порцій: "))
price_per_portion = float(input("Введіть ціну за порцію: "))


total_order_cost = quantity * price_per_portion


tax_rate = 0.18  
tip_rate = 0.14  

tax_amount = total_order_cost * tax_rate
tip_amount = total_order_cost * tip_rate

total_payment = total_order_cost + tax_amount + tip_amount

print("\nРахунок:")
print(f"Страва: {dish_name}")
print(f"Кількість порцій: {quantity}")
print(f"Ціна за порцію: {price_per_portion:.2f}")
print(f"Вартість замовлення: {total_order_cost:.2f}")
print(f"Податок (18%): {tax_amount:.2f}")
print(f"Чайові (14%): {tip_amount:.2f}")
print(f"Загальна сума для оплати: {total_payment:.2f}")
