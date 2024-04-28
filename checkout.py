from datetime import datetime
import array as arr

customers_name = input("What is the customer's name?: " '\n')

product_name = input("What did the user buy?: " '\n')
all_products= []
all_products.append(product_name)

quantity_bought = int(input("How many pieces?: " '\n'))
all_quantity = []
all_quantity.append(quantity_bought)

price_per_unit = int(input("How much per unit?: " '\n'))
all_prices = []
all_prices.append(price_per_unit)

add_more = input("Add more items?: " '\n')

while (add_more == 'yes'):
	product_name = input("What did the user buy?: " '\n')
	all_products= []
	all_products.append(product_name)

	quantity_bought = int(input("How many pieces?: " '\n'))
	all_quantity = []
	all_quantity.append(quantity_bought)

	price_per_unit = int(input("How much per unit?: " '\n'))
	all_prices = []
	all_prices.append(price_per_unit)

	
	add_more = input("Add more items?: " '\n')

	if add_more == 'no':
		break

cashier_name = input("What is your name?: " '\n')

discount_given = int(input("How much discount will he get?: " '\n'))


print('SEMICOLON STORES')
print('MAIN BRANCH')
print('LOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.')
print('TEL: 07048840550')
now = datetime.now()
print("Date:", now)
print("Cashier: ", cashier_name)
print("Customer Name: ", customers_name)

print('==============================================================')

print("    ", "ITEM",  "        ",  "QUANTITY",  "        ",  "PRICE", "        " 
, "TOTAL" )

print("--------------------------------------------------------------")

product = 0
bill_total = 0.0
discount = 0.0
VAT_amount = 0.0  


for i in all_products:
	print("    ", all_products, all_quantity, all_prices,   all_prices (all_quantity))

