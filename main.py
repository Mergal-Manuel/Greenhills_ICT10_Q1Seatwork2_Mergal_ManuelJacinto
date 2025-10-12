#Data types in python
from pyscript import display


restaurant_name = 'Mergals Table' #string
owner_name = 'Mergal' #string
year_established = 2013 #integer
popular_item_price = 139 #integer
has_delivery = True #boolean
product_names = ['bibimbap', 'Siomai rice', 'Siopao', 'Soopong noodles', 'Chow Mein'] #list
business_hours = '3am-6pm' #string
menu_prices = ['99 php', '49 php', '149 php', '179 php'] #list
common_allergens = ['Wheat', 'Egg', 'Soy'] #list
tax_rate = 0.05 #float

display(f'Welcome to the official site of {restaurant_name}! This was founded {year_established} by {owner_name} for his love of oriental cuisine.', target='infotext')
display(f'Hungry? here is a exclusive offer for exactly those who clicked the Home page! Claim your {product_names[0]} for only {popular_item_price} PHP instead of {menu_prices[3]} in the button above!', target='infotext2')
