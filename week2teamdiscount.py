print('Shop discounts on given weekdays')

# CORE REQUIREMENTS
print()

# Import the datetime function from the datetime module/ library
from datetime import datetime

# Assign the today's date to the variable current_date and week_day
current_date = datetime.now()
week_day = current_date.weekday()

print(f'Today is: {current_date}.')
print(f'The weekday is: {week_day}.')

# Ask subtotal from user
subtotal = float(input("What is the customer's subtotal? "))

# Use this logic to compute the discount and tax accordingly
if (week_day == 1 or week_day == 2) and subtotal >= 50:
    discounted_amount = subtotal - subtotal * .1
    sales_tax = discounted_amount * .06
    total = discounted_amount + sales_tax
    print(f'Thank you, on Tuesdays and Wednesdays you get a 10% discount. The sales tax is ${sales_tax:.2f} and the \
total is ${total:.2f}.')

else:
    discounted_amount = subtotal - 0
    sales_tax = discounted_amount * .06
    total = discounted_amount + sales_tax
    print(f'Please note a 10% discount is available on Tuesdays and Wednesdays only. The sales tax is ${sales_tax:.2f} and \
the total is ${total:.2f}.')

# NOTE: to test the program, change dates manually on your computer and chec discounts for Tuesday and Wednesday.


# # STRETCH REQUIREMENTS
# print()
# # Import the datetime function from the datetime module/ library
# from datetime import datetime

# # Assign the today's date to the variabel current_date
# # Temporarily use the week_day variable when checking which day has a discount. Change it from 0 to 6
# current_date = datetime.now()
# week_day = 2

# print(f'Today is: {current_date}.')
# print(f'The weekday is: {week_day}.')

# # STRETCH REQUIREMENT 2, Line 50 to 66
# # This code block will allow the user to enter how many items they are purchasing and the subtotal, then discount accordingly
# # Remember the while always starts with zero variables and an empty list as needed, then item prices are appended to the list

# cart = []
# shopping = ''
# subtotal = 0
# while shopping.lower() != 'done':
#     print('Please enter the item price and the quantity of the item you would like to purchase.')
#     price = float(input('What is the item price? '))
#     quantity = int(input('How many of these items would like to buy? '))
#     subtotal = price * quantity
#     cart.append(subtotal)

#     shopping = input('Would you like to keep shopping (Enter "Done" when finished and "Yes" to continue.)? ')

# cart_total = sum(cart)

# # Use the following logic to conduct the correct computations
# if (week_day == 1 or week_day == 2):
#     if cart_total >= 50:
#         discounted_amount = cart_total - cart_total * .1
#         sales_tax = discounted_amount * .06
#         total = discounted_amount + sales_tax
#         print(f'Thank you, on Tuesdays and Wednesdays you get a 10% discount. The sales tax is ${sales_tax:.2f} and the \
# total is ${total:.2f}.')
#     else: # Stretch requirement 1, Line 76 to 80. This tells the user how more they need to spend before geting a dscount
#         if subtotal < 50:
#             shortfall = 50 - cart_total
#             print(f'On Tuesdays and Wednesdays, we offer a 10% discount for purchases of $50.00 or greater. You have a \
# shorfall of ${shortfall:.2f}.')

# else:
#     discounted_amount = cart_total - 0
#     sales_tax = discounted_amount * .06
#     total = discounted_amount + sales_tax
#     print(f'Please note a 10% discount is available on Tuesdays and Wednesdays only. The sales tax is ${sales_tax:.2f} and \
# the total is ${total:.2f}.')


