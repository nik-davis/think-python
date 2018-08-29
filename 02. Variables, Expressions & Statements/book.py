retail_price = 24.95
discount = 0.40
discount_amount = retail_price * discount
discount_price = round(retail_price - discount_amount, 2)

books_ordered = 60
books_cost = 60 * discount_price

shipping = 3 + (0.75 * books_ordered)

total_price = books_cost + shipping

print(total_price)