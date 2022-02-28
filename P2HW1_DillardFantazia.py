# Get price input from users
#Write program to get subtotal,sales tax and total price
# Date: 28/Feb/2022
# CTI-110 P2HW1 - Total Purchases
# Fantazia Dillard
#


price_item_1 = float(input('Enter price for item 1:'))
price_item_2 =  float(input('Enter price for item 2:'))
price_item_3 = float(input('Enter price for item 3:'))
price_item_4 = float(input('Enter price for item 4:'))
price_item_5 =  float(input('Enter price for item 5:'))

subtotal = price_item_1 + price_item_2 + price_item_3 + price_item_4 + price_item_5
sales_tax = (subtotal * .07)
total_price = subtotal + sales_tax

print(f'Subtotal:{subtotal:.2f}')
print(f'Sales Tax:{subtotal*sales_tax:.2f}')
print(f'Total Prices: {total_price:.2f}')
