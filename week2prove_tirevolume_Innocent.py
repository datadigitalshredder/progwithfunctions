# Print what this program does
print('Tire volumes and prices at FIRESTONE by Innocent Hove')

# Import the math and datetime module
import math
from datetime import datetime
print()

# Making it my own: Provide user with the below range of tire sizes from Firestone, https://www.firestonetire.com/size# , \
# adding funtionality to add to shopping list then displaying the prize and subtotal. The while loop allows the user to add \
# more items.

# Name the variables before entering the loop
keep_shopping = ''
subtotal = 0
while keep_shopping.lower() != 'done':
    print('Welcome to our store. Please select tire properties from the provided: \n1. Size 35/12.5R20 \n2. Size 175/65R15 \n3. Size 255/65R18 \n4. Size 305/35R20 \n5. Size 325/30R19')
    print()

    # Request variables inputs, as stated above, from the user
    tire_width = float(input('What is the tire width in millimeters from any one item above? '))
    aspect_ratio = float(input('What is the aspect ratio of the tire from any one item above? '))
    wheel_diameter = float(input('What is the wheel diameter in inches from any one item above? '))

    print()
    # Compute the volume of tire
    volume_inside_tire = round((math.pi * tire_width ** 2 * aspect_ratio * (tire_width * aspect_ratio + 2540 * wheel_diameter)) / 10000000000, 2)
    # Display volume to the user
    print(f'The volume of inside space for this wheel is: \n{volume_inside_tire:.2f} liters.')
    print()
    # Compute appropriate tire prices as provided
    if volume_inside_tire == 0.25:
        print(f'The volume of the tire is {volume_inside_tire}, and the prize is $418.99.')
        quantity = int(input('How many items on this line would like? '))
        price = float(quantity * 418.99)
        print(f'The line total for these items is ${price:.2f}.')
        purchase = input('Do you want to purchase this item (YES or NO)? ')
    elif volume_inside_tire == 30.94:
        print(f'The volume of the tire is {volume_inside_tire}, and the prize is $102.99.')
        quantity = int(input('How many items on this line would like? '))
        price = float(quantity * 102.99)
        print(f'The line total for these items is ${price:.2f}.')
        purchase = input('Do you want to purchase this item (YES or NO)? ')
    elif volume_inside_tire == 82.72:
        print(f'The volume of the tire is {volume_inside_tire}, and the prize is $197.99.')
        quantity = int(input('How many items on this line would like? '))
        price = float(quantity * 197.99)
        print(f'The line total for these items is ${price:.2f}.')
        purchase = input('Do you want to purchase this item (YES or NO)? ')
    elif volume_inside_tire == 62.88:
        print(f'The volume of the tire is {volume_inside_tire}, and the prize is $307.99.')
        quantity = int(input('How many items on this line would like? '))
        price = float(quantity * 307.99)
        print(f'The line total for these items is ${price:.2f}.')
        purchase = input('Do you want to purchase this item (YES or NO)? ')
    elif volume_inside_tire == 57.75:
        print(f'The volume of the tire is {volume_inside_tire}, and the prize is $355.99.')
        quantity = int(input('How many items on this line would like? '))
        price = float(quantity * 355.99)
        print(f'The line total for these items is ${price:.2f}.')
        purchase = input('Do you want to purchase this item (YES or NO)? ')
    else:
        print("That's an invalid input, please enter tire properties stated.")
        print()
        price = 0 # If the user enters values not listed above, an invalid prompt is returned and total of the invalid line is not included.
        purchase = '' # Since the user was invalid, input to purchase or not must not be required.
    if purchase.lower() == 'yes':
        subtotal += price
        # Extract date from the computer
        current_date = datetime.now()

        # Open a file named "volume.txt" in append mode
        with open('volume.txt', 'at') as tire_details:
            # purchase = input('Do you want to purchase this item (YES or NO)? ')
            # if purchase.lower() == 'yes':
                # Print the appended values in one line. The total is the CUMULATIVE TOTAL of all valid items currently added to the cart. Also ask for their mobile number.
                mobile_number = int(input('Please enter your mobile number:'))
                print(f'Date:{current_date:%d-%m-%Y}, Width:{tire_width} mm, Aspect ratio:{aspect_ratio}, Diameter:{wheel_diameter} in, Volume:{volume_inside_tire:.2f} liters, Quantity: {quantity}, Line total ${price}, Total:${subtotal}, Mobile number {mobile_number}', file=tire_details)
    else:
        print('Please proceed to select next item.')
    
    keep_shopping = input('Do you want to keep shopping (Enter "DONE" when finished or "YES" to continue)? ') # Go to top of loop

print()
print(f'The total price for the items on your cart is ${subtotal:.2f}.') # Finally display the totol of items purchased
print()