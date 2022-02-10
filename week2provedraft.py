# Print what this progaram does
print('Tire Prices by FIRESTONE')

# Import the math module
import math
from datetime import datetime
print()

# Making it my own: Provide user with the below range of tire sizes from Firestone, https://www.firestonetire.com/size# , \
# adding to shopping cart then displaying the prize and subtotal. The while loop allows the user to add more items to the cart.

print('Welcome to our store. Please select tire properties from the provided. \n1. Size 35/12.5R20 \n2. Size 175/65R15 \n3. \
Size 255/65R18 \n4. Size 305/35R20 \n5. Size 325/30R19')
print()

# Request variables from the user
tire_width = float(input('What is the tire width in millimeters from any one item above? '))
aspect_ratio = float(input('What is the aspect ratio of the tire from any one item above? '))
wheel_diameter = float(input('What is the wheel diameter in inches from any one item above? '))

print()
# Compute the volume at once
volume_inside_tire = round((math.pi * tire_width ** 2 * aspect_ratio * (tire_width * aspect_ratio + 2540 * wheel_diameter)) / 10000000000, 2)
# Display volume to the user
print(f'The volume of space inside wheel is: \n {volume_inside_tire:.2f} liters.')
print()

if volume_inside_tire == 0.25:
    print(f'The volume of the tire is {volume_inside_tire}, and the prize is $418.99.')
elif volume_inside_tire == 30.94:
    print(f'The volume of the tire is {volume_inside_tire}, and the prize is $102.99.')
elif volume_inside_tire == 82.72:
    print(f'The volume of the tire is {volume_inside_tire}, and the prize is $197.99.')
elif volume_inside_tire == 62.88:
    print(f'The volume of the tire is {volume_inside_tire}, and the prize is $307.99.')
elif volume_inside_tire == 57.75:
    print(f'The volume of the tire is {volume_inside_tire}, and the prize is $355.99.')
else:
    print("That's an invalid input, please enter tire properties stated.")
print()

# Name the variables before entering the loop

keep_shopping = ''
quantity = 0
item = 0
subtotal = 0
while keep_shopping.lower() != 'done':
    print('Please select item NUMBER to add to cart: \n1. Size 35/12.5R20 \n2. Size 175/65R15 \n3. Size 255/65R18 \n4. Size 305/35R20 \n5. Size 325/30R19')
    item = int(input('Please enter item NUMBER to select tire size of your choice: '))
    if item == 1:
        quantity = int(input('How many items on this line would like? '))
        price = float(quantity * 418.99)
        print(f'The line total for these items is ${price:.2f}.')
    elif item == 2:
        quantity = int(input('How many items on this line would like? '))
        price = float(quantity * 102.99)
        print(f'The line total for these items is ${price:.2f}.')
    elif item == 3:
        quantity = int(input('How many items on this line would like? '))
        price = float(quantity * 197.99)
        print(f'The line total for these items is ${price:.2f}.')
    elif item == 4:
        quantity = int(input('How many items on this line would like? '))
        price = float(quantity * 307.99)
        print(f'The line total for these items is ${price:.2f}.')
    elif item == 5:
        quantity = int(input('How many items on this line would like? '))
        price = float(quantity * 355.99)
        print(f'The line total for these items is ${price:.2f}.')
    else:
        print("That's an invalid input, Please enter item numbers 1 to 5.")
    keep_shopping = input('Do you want to keep shopping (Enter "DONE" when finished or "YES" to continue)? ')
    subtotal += price

print(f'The total price for the items on your cart is ${subtotal:.2f}.')

# Extract date from the computer
current_date = datetime.now()

# Open a file named "volume.txt" in append mode
with open('volume.txt', 'at') as tire_details:

    # Print the appended values in one line
    print(f'{current_date:%d-%m-%Y}, {tire_width}, {aspect_ratio}, {wheel_diameter}, {volume_inside_tire:.2f} liters, ${subtotal}', file=tire_details)
