print('\nGutsai Stores\nBy Innocent Hove')

import csv
import random
from datetime import datetime

def main():
    try:
        products = read_products('products.csv')

        for i in products:
            item = products[i]
            # print(i, item)

        # Opening the request file for reading
        with open('request.csv', 'rt') as request:
            
            # Skipping the heading in the file
            reader = csv.reader(request)
            next(reader)

            # Loop through the request file and access the product name from the products dictionary
            QUANTITY = 1

            print('\nThe requested items are:')
            
            total_items = 0
            subtotal = 0
            for row in reader:
                item_ref = row[0] # Save the requested item key i.e. row[0] into a variable
                product_quantity = int(row[QUANTITY]) # Save the quantity of the item into a variable
                # stock_level = random_numbers() # Call the random numbers function and save the random number in a variable
                item = products[item_ref] # Use the item_ref to find the product details from the product dictionary
                product_name = item[0] # Use the item detail (list) to access the name 
                product_name_cap = product_name.capitalize()
                product_price = float(item[1]) # and the price

                print(f'{product_name_cap:14}: {product_quantity} @ ${product_price:5} each.')
                total_items += product_quantity
                subtotal += product_quantity * product_price
                
            print(f'\nTotal items requested is {total_items}. \nThe subtotal for the items is ${subtotal:.2f}.')

            tax = subtotal * .06
            print(f'\nSales tax is ${tax:.2f}. \nAmount due (including tax) is ${subtotal + tax:.2f}')

            print(f'\nThank you for shopping at Gutsai Stores, \nEnjoy the rest of your day!')

            # Call the now() method to get the current date and
            # time as a datetime object from the computer's clock.
            current_date_and_time = datetime.now()

            # Print the current day of the week and the current time.
            print(f"{current_date_and_time:%a %b %d, %Y; %I:%M:%S %p}\n")

            # print('\nMAKING IT MY OWN. \nAssume that stock levels are running low in the store and are constantly being adjusted. \nIt could be possible that the customer is told that there a fewer items left but when they attempt to buy later \nit would be possilbe in the event that stocks were adjusted up.\n\nThe requested items are:')
            
            # total_items1 = 0
            # subtotal1 = 0
            # for row1 in reader:
            #     item_ref1 = row1[0] # Save the requested item key i.e. row[0] into a variable
            #     product_quantity1 = int(row1[QUANTITY]) # Save the quantity of the item into a variable
            #     stock_level1 = random_numbers() # Call the random numbers function and save the random number in a variable
            #     item1 = products[item_ref1] # Use the item_ref to find the product details from the product dictionary
            #     product_name1 = item1[0] # Use the item detail (list) to access the name 
            #     product_name_cap1 = product_name1.capitalize()
            #     product_price1 = float(item1[1]) # and the price
            #     # print(stock_level)

            #     if stock_level1 >= product_quantity1: # When there are enough items left in stock...
            #         print(f'{product_name_cap1}: {product_quantity1} @ ${product_price1} each.')
            #         total_items1 += product_quantity1
            #         subtotal += product_quantity * product_price
            #         product_quantity1 -= product_quantity1
                
            #     else: # When there are not enough items left in stock, inform the user
            #         print(f'{product_name_cap}, there are only {stock_level1} items left in store. \n You will get {stock_level1} {product_name1} instead @ ${product_price1} each.')
            #         total_items1 += product_quantity1
            #         subtotal1 += stock_level1 * product_price1
            #         product_quantity1 = 0
                    

            # print(f'\nThe total number of items requested is {total_items}. \nThe subtotal for the items is ${subtotal:.2f}.')

            # tax = subtotal * .06
            # print(f'\nSales tax is ${tax:.2f}. \nAmount due (including tax) is ${subtotal + tax:.2f}')

            # print(f'\nThank you for shopping at Gutsai Stores, \nEnjoy the rest of your day!')

            # # Call the now() method to get the current date and
            # # time as a datetime object from the computer's clock.
            # current_date_and_time = datetime.now()

            # # Print the current day of the week and the current time.
            # print(f"{current_date_and_time:%a %b %d %I:%M:%S %Y}\n")

    except FileNotFoundError as not_found:
        print(f'{not_found}.\nThe file you entered was not found.')
    
    except PermissionError as perm_error:
        print(f'{perm_error}. \nYou do not have permission to access this file.')

    except KeyError as key_error:
        print(f'{key_error}. \nThe key entered is not on the store list.')
        
def read_products(products):
    """Opens and reads the the products.csv file and saves the information in the dictionary named products
    Parameters:
        products: The dictionary that will be populated
    Return:
        Products dictionary
    """
    products = {}

    # Open and read the products csv file
    with open("products.csv", "rt") as cart:

        # Create a reader module to skip the header of the csv file
        items = csv.reader(cart)
        next(items)

        # Retrieve items from each row in the csv file and add to the dictionary
        for row in items:
            product_number = row[0]
            product_name = row[1]
            price = float(row[2])

            products[product_number] = [product_name, price]
    return products

# def random_numbers():
#     """Generates random interger numbers between 0 and 10
#     Parameters:
#         None
#     Return value:
#         A random number
#     """

#     number = random.randint(1,5)
#     return number

if __name__ == "__main__":
    main()
            